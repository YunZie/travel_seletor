  
from rest_framework import serializers
from applications.models import *
 
 
class SeriesSerializers(serializers.ModelSerializer):
	def create(self, validated_data):
		return series.objects.create(**validated_data)

	class Meta:
		model = series
		fields = (
			'short_key',
			'url',
			'create_time',
			'iskeepforever',
		)

class CitySerializers(serializers.ModelSerializer):
	def create(self, validated_data):
		return city.objects.create(**validated_data)

	class Meta:
		model = city
		fields = (
			'short_key',
			'url',
			'create_time',
			'iskeepforever',
		)

class ItemsSerializers(serializers.ModelSerializer):
	def create(self, validated_data):
		return items.objects.create(**validated_data)

	class Meta:
		model = items
		fields = (
			'short_key',
			'url',
			'create_time',
			'iskeepforever',
		)

