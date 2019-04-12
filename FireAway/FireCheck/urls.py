from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns =[
    path("", views.index, name="index"),
    #path("login", LoginView.as_view(template_name="FireCheck/login.html"), name="login"),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("devicelist", views.device_list, name="devicelist"),
    path("buildinglist", views.building_list, name="buildinglist"),
    path("zonelist", views.zone_list, name="zonelist"),
    path("addpanel", views.panel_list, name="panellist"),
    path("adddevice", views.panel_list, name="panellist"),
    path("addzone", views.panel_list, name="panellist"),
    path("addbuilding", views.panel_list, name="panellist"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("create", views.create, name="create"),
    #path("panellist", views.panel_list, name="panellist"),
]
