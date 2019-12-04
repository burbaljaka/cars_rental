from rest_framework import serializers
from .views import Car
from django.contrib.auth.models import User
from rental.models import Car

class UserAndCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_issue_year']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserCarSerializer(serializers.ModelSerializer):
    modules = UserAndCarSerializer(many = True, read_only = True)

    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_issue_year', 'modules']
