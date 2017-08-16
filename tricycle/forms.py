from .models import Operator,Driver
from django import forms
from django.contrib.auth.models import User
import datetime
class OperatorForm(forms.ModelForm):
	gender = (
    ('M', 'Male'),
    ('F', 'Female'),
	)
	gender = forms.ChoiceField(widget=forms.Select(),choices = gender);
	date_registered = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}));
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	age = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	
	class Meta():
		model = Operator
		fields = ['first_name','last_name','age','gender','address','date_registered','image']
class DriverForm(forms.ModelForm):
	gender = (
    ('M', 'Male'),
    ('F', 'Female'),
	)
	gender = forms.ChoiceField(widget=forms.Select(),choices = gender);
	date_registered = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}));
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	age = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta():
		model = Driver
		fields = ['first_name','last_name','age','gender','address','date_registered','image']
			
class UserForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput);
	class Meta:
		model = User
		fields = ['username','password']


			
		