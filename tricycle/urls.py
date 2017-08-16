"""Bactoda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views,logout
from django.contrib import admin
app_name = 'tricycle'
urlpatterns = [
    
    url(r'^logout/',include(admin.site.urls)),
    url(r'^$',views.OperatorIndexView.as_view(),name="index"),
    url(r'^operator/(?P<pk>[0-9]+)$',views.DetailView.as_view(),name="details"),
    url(r'^operator/add/$',views.OperatorCreate.as_view(),name='add'),
    url(r'^operator/(?P<pk>[0-9]+)/$',views.OperatorUpdate.as_view(),name='edit'),
    url(r'^operator/(?P<pk>[0-9]+)/delete/$',views.OperatorDelete.as_view(),name='delete'),
    #Drivermodel
    url(r'^driver/$',views.DriverIndexView.as_view(),name="driver-index"),
    url(r'^driver/(?P<pk>[0-9]+)$',views.DriverDetailView.as_view(),name="driver-details"),
    url(r'^driver/add/$',views.DriverCreate.as_view(),name='driver-add'),
    url(r'^driver/(?P<pk>[0-9]+)/$',views.DriverUpdate.as_view(),name='driver-edit'),
    url(r'^driver/(?P<pk>[0-9]+)/delete/$',views.DriverDelete.as_view(),name='driver-delete'),
    #TricycleModel
    url(r'^tricycle/$',views.TricycleIndexView.as_view(),name="tricycle-index"),
    url(r'^tricycle/(?P<pk>[0-9]+)$',views.TricycleDetailView.as_view(),name="tricycle-details"),
    url(r'^tricycle/add/$',views.TricycleCreate.as_view(),name='tricycle-add'),
    url(r'^tricycle/(?P<pk>[0-9]+)/$',views.TricycleUpdate.as_view(),name='tricycle-edit'),
    url(r'^tricycle/(?P<pk>[0-9]+)/delete/$',views.TricycleDelete.as_view(),name='tricycle-delete'),
]
