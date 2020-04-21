from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from django import core
from django.http import JsonResponse, HttpResponse, QueryDict
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.core.files.storage import default_storage
from django.forms.models import model_to_dict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action

import json
import os
import re
import coreapi

from applications.crawler import all_key
from applications.models import city, items, series
from applications.serializers import *	


def trans_data_format(all_data : list, allow_columns : dict) -> list:
    result = []
    for element in all_data:
        _dict = {}
        for key, value in element.items():
            if key in allow_columns.keys():
                _dict[allow_columns.get(key)] = value
        result.append(_dict)
    return result

class Date_Processor(APIView):
    def get(self, request):
        return HttpResponse("")

    def post(self, request):
        with open('./dist/weather.json', 'rb+') as f:
           all_data = json.load(f)
        print(request.data)
        city_allow_columns = {
            'city' : 'city', 
            'location' : 'district', 
            'lat' : 'latitude', 
            'lon' : 'longitude'
        }
        city_data = trans_data_format(all_data, city_allow_columns)
        city_data = [dict(t) for t in {tuple(d.items()) for d in city_data}]
        
        # city_serializers = CitySerializers(data=city_data, context=request, many=True)
        # if not city_serializers.is_valid():
        #     return Response(city_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # city_serializers.save()

        items_allow_columns = {
            'description' : 'description', 
            'elementName' : 'element_name', 
        }
        items = trans_data_format(all_data, items_allow_columns)
        items = [dict(t) for t in {tuple(d.items()) for d in items}]

        # items_serializers = ItemsSerializers(data=items, context=request, many=True)
        # if not items_serializers.is_valid():
        #     return Response(items_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # items_serializers.save()

        series_allow_columns = {
            'measures' : 'measure', 
            'value' : 'value', 
            'startTime' : 'start_time', 
            'endTime' : 'end_time',
            'time_unit' : 'time_unit',
            'location' : 'city_id',  #代替
            'elementName' : 'items_id',  #代替
        }
        series = trans_data_format(all_data, series_allow_columns)
        
        # series_serializers = SeriesSerializers(data=series, context=request, many=True)
        # if not series_serializers.is_valid():
        #     return Response(series_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # series_serializers.save()

        return JsonResponse(items,safe=False)

    def delete(self, request):
        return ""