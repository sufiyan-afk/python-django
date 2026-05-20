from django.urls import path
from registration.views import *

urlpatterns = [
    path('',index,name="index"),
    path("reg",reg,name="reg")
]