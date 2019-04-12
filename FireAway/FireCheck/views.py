from django.shortcuts import render
from django.shortcuts import Http404,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#from .data import building_data
from .models import *
from django.contrib.auth.models import User,Group

def create(request):
    #building_data()
    context= {
        "buildings" : building.objects.all()
    }
    return render(request, "FireCheck/buildinglist.html", context)

def index(request):
    context = {

    }
    return render(request, "FireCheck/dashboard.html", context)

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
#def create_panel(return):
#    if request.POST:
#        accep = panel(request.POST['building'])

#def login(request):
     #username = request.POST['username']
     #password = request.POST['password']
     #user = authenticate(request, username=username, password=password)
     #if user is not None:
         #if login(request, user):
                #context= {
                #    "buildings" : building.objects.all()
                #    }
                #return render(request, "FireCheck/buildinglist.html", context)

#     else:
#return render(request, "FireCheck/login.html",{})
