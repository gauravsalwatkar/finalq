from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
    path('result/',views.result,name='result'),
    path('home/',views.home,name='home'),
]