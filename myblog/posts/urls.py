from unicodedata import name
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
