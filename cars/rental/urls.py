from django.conf.urls import url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include
from rest_framework import routers
from . import views

app_name = "rental"

urlpatterns = (
    path('cars/', views.car_list, name = 'cars_list'),
    path('client_cars/', views.client_Loan_Cars, name = 'client_cars'),
    path('car/<int:pk>/', views.car_detail, name = 'car_detail'),

)
