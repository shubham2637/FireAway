from django.urls import path
from . import views

urlpatterns =[
    path("Login", views.index, name="index"),
    path("devicelist", views.device_list, name="devicelist"),
    path("buildinglist", views.building_list, name="buildinglist"),
    path("zonelist", views.zone_list, name="zonelist"),
    path("panellist", views.panel_list, name="panellist")
]
