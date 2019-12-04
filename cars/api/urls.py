from django.urls import path
from api.views import CarListView, UserListView
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('cars', CarListView)

urlpatterns = [
    path('cars/', CarListView.as_view(), name = 'cars'),
    path('users/', UserListView.as_view(), name = 'users'),
    # path('users/<pk>/', UserCarsListView.as_view(), name = 'usercars'),
]
