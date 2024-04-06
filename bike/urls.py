from django.urls import path
from bike.views import *

app_name='bike'

urlpatterns=[
    path('tvsxl/',tvsxl,name='tvsxl'),
]