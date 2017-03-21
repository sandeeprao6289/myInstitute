from django import forms
from django.conf import settings

from usermgmt.models import User

class UserForm(forms.ModelForm):
	first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	email = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))

	class Meta:
		model = User
		fields = ('first_name','last_name', 'email')
