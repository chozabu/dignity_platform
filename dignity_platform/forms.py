"""Foobar.py: Description of what foobar does."""

__author__ = "Alex 'Chozabu' P-B"
__copyright__ = "Copyright 2016, IAgree"

import django
from .models import Person, JobHirer, JobWorker

class UserForm(django.forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ServiceForm(django.forms.ModelForm):
    class Meta:
        model = JobWorker
        fields = ['job', 'price']



class HirerForm(django.forms.ModelForm):
    class Meta:
        model = JobHirer
        fields = ['job', 'price']
