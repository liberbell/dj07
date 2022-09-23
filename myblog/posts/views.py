from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello world. This is a index page.")
    return render(request, "posts/index.html")