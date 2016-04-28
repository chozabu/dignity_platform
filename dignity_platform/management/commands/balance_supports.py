"""balance_supports.py: balance support of users up to 51%."""

__author__ = "Alex 'Chozabu' P-B"
__copyright__ = "Copyright 2016, Chozabu"

from django.core.management.base import BaseCommand, CommandError
from dignity_platform.models import Person, CauseSupporter

import time

class Command(BaseCommand):
    help = 'Runs some API methods'

    def add_arguments(self, parser):
        # parser.add_argument('update', nargs='+', type=dict)
        #parser.add_argument('question_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        print(args)
        print(options)
        for u in Person.objects.all():
            cs = CauseSupporter.objects.balance_user_support(u, u.self_support)
            print(cs)
