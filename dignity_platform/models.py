from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager


# Create your models here.



class Person(AbstractUser):
	pass


class Cause(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)

class Job(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)


class JobWorker(models.Model):
	person = models.ForeignKey(Person, related_name='jobs_i_will_do')
	job = models.ForeignKey(Job, related_name='workers')
	def __str__(self):
		return str(self.person) + " offers " + str(self.job)


#class Desire(models.Model):
#	name = models.CharField(max_length=200)
