from django.conf.urls import url
from django.urls import path
from rental import views

app_name = "rental"

urlpatterns = [
    path('cars/', views.car_list, name = 'cars_list'),
    path('client_cars/', views.client_Loan_Cars, name = 'client_cars'),
    path('car/<pk>/', views.CarDetailView.as_view(), name = 'car_detail')
]
