from rest_framework import serializers
from .views import Car
from django.contrib.auth.models import User
from rental.models import Car

class UserAndCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_issue_year']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserAnsCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_issue_year']
