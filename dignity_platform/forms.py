"""Foobar.py: Description of what foobar does."""

__author__ = "Alex 'Chozabu' P-B"
__copyright__ = "Copyright 2016, IAgree"

import django
from .models import Person, JobHirer, JobWorker, CauseSupporter, Job, Cause

class UserForm(django.forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ServiceForm(django.forms.ModelForm):
    class Meta:
        model = JobWorker
        fields = ['job', 'price']
class SupportingForm(django.forms.ModelForm):
    class Meta:
        model = CauseSupporter
        fields = ['cause', 'amount']



class HirerForm(django.forms.ModelForm):
    class Meta:
        model = JobHirer
        fields = ['job', 'price']

class JobForm(django.forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name']

class CauseForm(django.forms.ModelForm):
    class Meta:
        model = Cause
        fields = ['name']
