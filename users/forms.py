from allauth.account.forms import SignupForm
from django import forms
from .models import *
from django.contrib import messages

class SimpleSignupForm(SignupForm):
    first_name = forms.CharField(max_length=12, label='First Name:')
    last_name = forms.CharField(max_length=12, label='Last Name:')

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        messages.warning(request, 'Message' )
        user.save()
        return user
