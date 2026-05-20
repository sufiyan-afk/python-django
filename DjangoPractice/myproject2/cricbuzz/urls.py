from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("scorecard/",views.scorecard),
    path("stats/",views.stats),
]