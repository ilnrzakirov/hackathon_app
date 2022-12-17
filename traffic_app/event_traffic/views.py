from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def register_to_event(request, pk):
    print(pk)
    return HttpResponse("ok")
