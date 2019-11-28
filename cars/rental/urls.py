from django.conf.urls import url
from django.urls import path
from rental import views
from django.conf.urls.i18n import i18n_patterns

app_name = "rental"

urlpatterns = (
    path('cars/', views.car_list, name = 'cars_list'),
    path('client_cars/', views.client_Loan_Cars, name = 'client_cars'),
    path('car/<int:pk>/', views.car_detail, name = 'car_detail'),
)
