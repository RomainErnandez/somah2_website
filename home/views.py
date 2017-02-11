from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Period

def dashboard(request):
    return render(request, template_name='home/dashboard.html')

def view_period(request, id_period):
    try:
        period = Period.objects.get(id=id_period)
    except Exception as e:
        raise Http404
    else:
        return HttpResponse("period: " + str(period.id))

def user(request):
    return render(request, template_name='home/user.html')

def notifications(request):
    return render(request, template_name='home/notifications.html')

def table(request):
    return render(request, template_name='home/table.html')