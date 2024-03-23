from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    message="hi"
    return HttpResponse(message)
