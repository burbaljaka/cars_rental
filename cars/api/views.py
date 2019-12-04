from rest_framework import generics
from rental.models import Car
from django.contrib.auth.models import User
from . serializers import CarSerializer, UserSerializer, UserAndCarSerializer
from rest_framework.views import APIView

class CarListView(generics.ListAPIView):
    queryset = Car.objects.filter(car_status = 'a')
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCarsListView(APIView):
	queryset = Car.objects.filter(car_renter = pk, car_status = 'o')
	serializer_class = UserAndCarSerializer
