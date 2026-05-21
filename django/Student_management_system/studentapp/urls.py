from django.urls import path
from studentapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path('display',display,name = 'display'),
    path('update',update,name="update"),
    path("delete",delete,name="delete")
]