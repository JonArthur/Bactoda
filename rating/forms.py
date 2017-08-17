from .models import Rate
from django import forms

class RateForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}));
	comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Rate
		fields = ['name','comment','email','driver']
		
