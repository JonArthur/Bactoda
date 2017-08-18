from django.conf.urls import url,include
from django.conf import settings
from . import views
app_name = "rating"
urlpatterns = [
    url(r'^rate/(?P<pk>[0-9]+)$', views.rate,name="rate"),
    url(r'^$', views.IndexView.as_view(),name="index"),
    url(r'^search/', views.current_datetime,name="query")
    
]

