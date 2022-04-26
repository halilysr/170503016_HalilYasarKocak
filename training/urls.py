from django.contrib import admin
from django.urls import path
from . import views

app_name = "trainings"

urlpatterns = [
    path('create/',views.index,name="index"),
]