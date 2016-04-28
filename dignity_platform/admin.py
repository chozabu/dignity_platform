from django.contrib import admin

# Register your models here.

from . import models
from django.contrib.auth.admin import UserAdmin

class PersonAdmin(UserAdmin):
    pass

admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Cause)
admin.site.register(models.CauseSupporter)
admin.site.register(models.Job)
admin.site.register(models.JobWorker)
admin.site.register(models.JobHirer)
