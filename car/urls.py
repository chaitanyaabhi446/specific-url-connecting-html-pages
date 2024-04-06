from django.urls import path
from car.views import *

app_name='car'

urlpatterns=[
    path('ambasdor/',ambasdor,name='ambasdor'),
]