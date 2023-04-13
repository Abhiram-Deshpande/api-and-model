from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def print_fun(request):
    
    return HttpResponse('{"key":"value"}', content_type='application/json')
