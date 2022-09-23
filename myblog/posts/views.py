from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse("Hello world. This is a index page.")
    posts = Post.objects.order_by("-publish_date")
    return render(request, "posts/index.html", {"posts": posts})
