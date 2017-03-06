from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
	name = models.TextField(max_length=100)
	twitter = models.TextField(max_length=32)
	
class Sobre(models.Model):
	amount = models.IntegerField()
	concept = models.TextField(max_length=100)
	date = models.DateTimeField()
	donor = models.ForeignKey(Donor)
	user = models.ForeignKey(User)
