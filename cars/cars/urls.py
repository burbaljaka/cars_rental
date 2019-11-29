"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rental import views
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('rosetta/', include('rosetta.urls')),
    path('rental/', include('rental.urls')),
    path('special/',views.special,name='special'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('api/', include('api.urls', namespace = 'api'))
)
