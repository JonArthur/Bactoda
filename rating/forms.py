from .models import Rate
from django import forms

class RateForm(forms.ModelForm):
	choices = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
	)
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}));
	comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
	email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	rating = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}),choices = choices);
	class Meta:
		model = Rate
		fields = ['name','comment','email']
		
