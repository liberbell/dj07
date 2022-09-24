from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/<int:post_id>[0-9]', views.)
]
