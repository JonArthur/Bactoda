from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Operator,Driver,Tricycle
from .forms import OperatorForm,DriverForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

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



# class UserFormView(View):
#     form_class = UserForm
#     template_name ='tricycle/registration_form.html'
#     def get(self,request):
#         form = self.form_class(None)
#         return render(request,self.template_name,{'form':form})
#         pass

#     def post(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user = authenticate(username=username,password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return redirect('tricycle:index')
        

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('tricycle:index')
        

#     return render(request,self.template_name,{'form':form})