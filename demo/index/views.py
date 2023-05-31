from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("welcome django")
    

# Create your views here.
