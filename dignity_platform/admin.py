from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Person)
admin.site.register(models.Cause)
admin.site.register(models.CauseSupporter)
admin.site.register(models.Job)
admin.site.register(models.JobWorker)
admin.site.register(models.JobHirer)
