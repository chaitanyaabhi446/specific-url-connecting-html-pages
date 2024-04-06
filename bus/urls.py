from django.urls import path
from bus.views import *

app_name='bus'

urlpatterns=[
    path('apsrtc/',apsrtc,name='apsrtc'),
]