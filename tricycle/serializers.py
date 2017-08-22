from rest_framework import serializers
from .models import Driver,Operator,Tricycle

class DriverSerializer(serializers.ModelSerializer):

	class Meta:
		model = Driver
		fields = '__all__'