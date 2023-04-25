from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    reponse = HttpResponse()
    reponse.write("<h5>Hello Worldasdasdasdasdasd</h5>")
    reponse.write("This is polls app ")
    return reponse