from . import views
from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/<int:post_id>[0-9]', views.post_detail, name="post_detail"),
]
