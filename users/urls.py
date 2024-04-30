from django.urls import path
from .views import *

urlpatterns = [
    path('1', get_info, name='get_info'),
]