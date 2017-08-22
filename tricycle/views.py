from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Operator,Driver,Tricycle
from .forms import OperatorForm,DriverForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DriverSerializer,OperatorSerializer


class OperatorIndexView(LoginRequiredMixin,generic.ListView):
    login_url = '/admin/login/'
    template_name = 'tricycle/operator/index.html'
    def get_queryset(self):
        return Operator.objects.all()
  
    def dispatch(self, request, *args, **kwargs):        
        return super(OperatorIndexView, self).dispatch(request, *args, **kwargs)
    
class DetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/admin/login/'
    model =Operator
    template_name = 'tricycle/operator/details.html'

class OperatorCreate(LoginRequiredMixin,generic.CreateView):
    login_url = '/admin/login/'
    form_class = OperatorForm
    model = Operator
    #fields = ['first_name','last_name','age','gender','address','date_registered','image']
    
class OperatorUpdate(generic.UpdateView):
    login_url = '/admin/login/'
    model = Operator
    form_class = OperatorForm

class OperatorDelete(LoginRequiredMixin,generic.DeleteView):
    login_url = '/admin/login/'
    model = Operator
    success_url = reverse_lazy('tricycle:index')

#Driver Views

class DriverIndexView(LoginRequiredMixin,generic.ListView):
    login_url = '/admin/login/'
    model = Driver
    template_name = 'tricycle/driver/index.html'
    def get_queryset(self):
        return Driver.objects.all()
class DriverDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/admin/login/'
    model = Driver
    template_name = 'tricycle/driver/details.html'
class DriverCreate(LoginRequiredMixin,generic.CreateView):
    login_url = '/admin/login/'
    model = Driver
    form_class = DriverForm
    #fields = ['first_name','last_name','age','gender','address','date_registered']  

class DriverUpdate(LoginRequiredMixin,generic.UpdateView):
    login_url = '/admin/login/'
    model = Driver
    form_class=DriverForm
    #fields = ['first_name','last_name','age','gender','address']

class DriverDelete(LoginRequiredMixin,generic.DeleteView):
    login_url = '/admin/login/'
    model = Driver
    success_url = reverse_lazy('tricycle:driver-index')


#Tricycle Views
 
class TricycleIndexView(LoginRequiredMixin,generic.ListView):
    login_url = '/admin/login/'
    model = Tricycle
    template_name = 'tricycle/tricycle/index.html'
    def get_queryset(self):
        return Tricycle.objects.all()


class TricycleDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/admin/login/'
    model = Tricycle
    template_name = 'tricycle/tricycle/details.html'
class TricycleCreate(LoginRequiredMixin,generic.CreateView):
    login_url = '/admin/login/'
    model = Tricycle
    fields = ['body_number','date_registered','operator','driver']

class TricycleUpdate(LoginRequiredMixin,generic.UpdateView):
    login_url = '/admin/login/'
    model = Tricycle
    fields = ['body_number','date_registered','operator','driver']

class TricycleDelete(LoginRequiredMixin,generic.DeleteView):
    login_url = '/admin/login/'
    model = Tricycle
    success_url = reverse_lazy('tricycle:index')



class DriverList(APIView):
    
    def get(self,request):
        driver = Driver.objects.all()
        serializer = DriverSerializer(driver,many=True)
        return Response(serializer.data)
        pass

    def post(self):
        pass
        
class OperatorList(APIView):
    
    def get(self,request):
        operator = Operator.objects.all()
        serializer = OperatorSerializer(operator,many=True)
        return Response(serializer.data)
        pass

    def post(self):
        pass        