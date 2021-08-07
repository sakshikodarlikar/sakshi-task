from django.urls import path, include
from django.contrib import admin

from . import views
urlpatterns = [
    path('', views.userList.as_view(), name='index'),
  #  path('',views.userList.as_view(),name='get'),
]