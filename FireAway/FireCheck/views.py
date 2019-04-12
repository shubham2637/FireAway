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
        "buildings" : building.objects.all(),
        "devices" : device.objects.all(),
        "td" : device.objects.all().count(),
        "gd" : device.objects.filter(health='G').count(),
        "rd" : device.objects.filter(health='R').count(),
        "yd" : device.objects.filter(health='Y').count(),

    }
    return render(request, "FireCheck/dashboard.html", context)

def device_details(request, did):
    context= {
        "d" : device.objects.get(pk=did)
    }
    return render(request, "FireCheck/device_details.html", context)


def zone_details(request, zid):
    zo=zone.objects.get(pk=zid)
    context= {
        "z" : zone.objects.get(pk=zid),
        "d" : device.objects.filter(zone=zo),
        "dc":device.objects.filter(zone=zo).count(),
    }
    return render(request, "FireCheck/zone_details.html", context)

def building_details(request, bid):
    bo=building.objects.get(pk=bid)
    context= {
        "b" : building.objects.get(pk=bid),
        "d" : device.objects.filter(building=bo),
        "dc":device.objects.filter(building=bo).count(),
        "z" : zone.objects.filter(building=bo),
        "zc":zone.objects.filter(building=bo).count(),
        "p" : panel.objects.filter(building=bo),
        "pc":panel.objects.filter(building=bo).count(),
    }
    return render(request, "FireCheck/building_details.html", context)

def panel_details(request, pid):
    po=panel.objects.get(pk=pid)
    context= {
        "p" : panel.objects.get(pk=pid),
        "d" : device.objects.filter(panel=po),
        "dc":device.objects.filter(panel=po).count(),
        "z" : zone.objects.filter(panel=po),
        "zc":zone.objects.filter(panel=po).count(),
    }
    return render(request, "FireCheck/panel_details.html", context)




def device_list(request):
    context= {
        "devices" : device.objects.all()
    }
    return render(request, "FireCheck/table.html", context)

def red_device_list(request):
    context= {
        "devices" : device.objects.all().filter(health='R')
    }
    return render(request, "FireCheck/table.html", context)


def green_device_list(request):
    context= {
        "devices" : device.objects.all().filter(health='G')
    }
    return render(request, "FireCheck/table.html", context)

def yellow_device_list(request):
    context= {
        "devices" : device.objects.all().filter(health='Y')
    }
    return render(request, "FireCheck/table.html", context)


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
