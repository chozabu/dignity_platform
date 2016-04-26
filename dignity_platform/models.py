from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager


# Create your models here.



class Person(AbstractUser):
	pass


class Cause(models.Model):
	name = models.CharField(max_length=200)

class Job(models.Model):
	name = models.CharField(max_length=200)


class JobWorker(models.Model):
	person = models.ForeignKey(Person, related_name='jobs_i_will_do')
	jobs = models.ForeignKey(Job, related_name='workers')


#class Desire(models.Model):
#	name = models.CharField(max_length=200)
