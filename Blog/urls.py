from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from . import views
urlpatterns = [
# 主页
path('', views.index, name='index'),
]