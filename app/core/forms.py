from django.core import validators
from django import forms
from .models import Contact

class ContactRegistration(forms.ModelForm):
 class Meta:
  model = Contact
  fields = ['name', 'email', 'subject', 'message']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control mt-2'}),
   'email': forms.EmailInput(attrs={'class':'form-control mt-2'}),
   'subject': forms.TextInput(attrs={'class':'form-control mt-2'}),
   'message': forms.TextInput(attrs={'class':'form-control mt-2'}),

  }
    