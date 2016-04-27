"""Foobar.py: Description of what foobar does."""

__author__ = "Alex 'Chozabu' P-B"
__copyright__ = "Copyright 2016, IAgree"

import django
from .models import Person

class UserForm(django.forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
