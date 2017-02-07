from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, template_name='home/home.html')

def view_period(request, id_period):
    if int(id_period) > 100:
        raise Http404
    return HttpResponse("" + id_period)