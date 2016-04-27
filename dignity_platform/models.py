from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager


# Create your models here.



class Person(AbstractUser):
	self_support = models.FloatField(default=.49)


class Cause(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)


from django.db.models import F, Sum
class CauseSupporterManager(models.Manager):
	def balance_user_support(self, person, reserved=.0):
		qs = self.get_queryset()
		qs = qs.filter(person=person)
		totalag = qs.aggregate(count=Sum('amount'))['count']
		if reserved: totalag = totalag/(1.-reserved)

		qs.update(amount=F('amount') /totalag)
		return qs

class CauseSupporter(models.Model):
	objects = CauseSupporterManager()
	amount = models.FloatField(default=0.1)
	person = models.ForeignKey(Person, related_name='causes_i_support')
	cause = models.ForeignKey(Cause, related_name='people_supporting_cause')
	def __str__(self):
		return str(self.person) + " supports " + str(self.cause) + " at " + str(self.amount * 100) + "%"

class Job(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)


class JobWorker(models.Model):
	person = models.ForeignKey(Person, related_name='jobs_i_will_do')
	job = models.ForeignKey(Job, related_name='workers')
	price = models.FloatField(default=15.0)
	def __str__(self):
		return str(self.person) + " offers " + str(self.job)

class JobHirer(models.Model):
	person = models.ForeignKey(Person, related_name='jobs_i_want_done')
	job = models.ForeignKey(Job, related_name='hirers')
	def __str__(self):
		return str(self.person) + " requests " + str(self.job)


#class Desire(models.Model):
#	name = models.CharField(max_length=200)
