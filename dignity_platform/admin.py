from django.contrib import admin

# Register your models here.

from .models import Person, Cause, Job, JobWorker, JobHirer

admin.site.register(Person)
admin.site.register(Cause)
admin.site.register(Job)
admin.site.register(JobWorker)
admin.site.register(JobHirer)
