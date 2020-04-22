from rest_framework import serializers
from applications.models import city, items, series
from rest_framework.validators import UniqueTogetherValidator
 
 
class SeriesSerializers(serializers.ModelSerializer):
	def create(self, validated_data):
		return series.objects.create(**validated_data)

	def validate(self, attrs):

		# Insert not duplicating data.
		time_unit = attrs.get('time_unit')
		city_id = attrs.get('city_id')
		items_id = attrs.get('items_id')
		measure = attrs.get('measure')

		try:
			get_db_val = series.objects.get(
				city_id = city_id,
				measure = measure,
				items_id = items_id,
				time_unit = time_unit,
				)
		except series.DoesNotExist:
			return series.objects.create(**attrs)
		if self.object and get_db_val.id == self.object.id:
			return series.objects.create(**attrs)
		else:
			raise serializers.ValidationError('already exists')

	class Meta:
		model = series
		fields = (
			'measure',
			'value',
			'start_time',
			'end_time',
			'city_id',
			'items_id',
			'time_unit',
		)


class CitySerializers(serializers.ModelSerializer):
	
	def create(self, validated_data):
		return city.objects.create(**validated_data)
	def validate(self, attrs):
		city_name = attrs.get('city')
		district = attrs.get('district')
		try:
			get_db_val = city.objects.get(
					city = city_name,
					district = district,
				)
		except city.DoesNotExist:
			return city.objects.create(**attrs)
		if self.object and get_db_val.id == self.object.id:
			return city.objects.create(**attrs)
		else:
			raise serializers.ValidationError('already exists')
		
	class Meta:
		model = city
		fields = (
			'city',
			'district',
			'longitude',
			'latitude',
		)

class ItemsSerializers(serializers.ModelSerializer):
	def create(self, validated_data):
		return items.objects.create(**validated_data)

	def validate(self, attrs):
		description = attrs.get('description')
		try:
			get_db_val = items.objects.get(
					description = description,
				)
		except items.DoesNotExist:
			return items.objects.create(**attrs)
		if self.object and get_db_val.id == self.object.id:
			return items.objects.create(**attrs)
		else:
			raise serializers.ValidationError('already exists')
	class Meta:
		model = items
		fields = (
			'description',
			'element_name',
		)
