from django.shortcuts import render
from django.shortcuts import Http404,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import *

def index(request):
    context = {

    }
    return render(request, "FireCheck/index.html", context)

def device_list(request):
    context= {
        "devices" : device.objects.all()
    }
    return render(request, "FireCheck/devicelist.html", context)

def building_list(request):
    context= {
        "buildings" : building.objects.all()
    }
    return render(request, "FireCheck/buildinglist.html", context)

def zone_list(request):
    context= {
        "zones" : zone.objects.all()
    }
    return render(request, "FireCheck/zonelist.html", context)

def panel_list(request):
    context= {
        "panels" : panel.objects.all()
    }
    return render(request, "FireCheck/panellist.html", context)
