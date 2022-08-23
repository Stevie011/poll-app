from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Harzit world, you're at le polls index")
