from django.urls import path
from . import views

urlpatterns = [
    path('', views.bin_operations, name='bins'),
]