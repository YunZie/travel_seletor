from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from django import core
from django.http import JsonResponse, HttpResponse, QueryDict
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.core.files.storage import default_storage
from django.forms.models import model_to_dict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.schemas import AutoSchema

import json
import os
import re
import coreapi

from crawler import all_key
from applications.models import *
from applications.serializers import *	


class Date_Processor(APIView):
    def get(self, request):
        return ""

    def post(self, request):
        all_key()
        cluster_serializers = WeatherSerializer(data=cluster_items, context=request, many=True)
        if not cluster_serializers.is_valid():
            return Response(cluster_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        return ""

    def delete(self, request):
        return ""