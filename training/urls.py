from django.contrib import admin
from django.urls import path
from . import views

app_name = "training"

urlpatterns = [
    path('', views.training, name='training'),
    path('addtraining', views.addtraining, name='addtraining'),
    path('dashboard/',views.dashboard,name="dashboard"),
]