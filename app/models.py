"""
Definition of models.
"""

from django.db import models

'''
from django import ModelForms
'''
# Create your models here


class Login_Check(models.Model):
	user_name = models.CharField("User Name", max_length=20);
	password = models.CharField("Password", max_length=15, default="password");
	shelter_check = models.CharField(max_length=200);

class Shelter_Information(models.Model):
	shelter_name = models.ForeignKey(Login_Check);
	shelter_address = models.CharField(max_length=1000);
	shelter_city = models.CharField("City", max_length=100);
	longitude = models.FloatField(max_length=200, default=0);
	latitude = models.FloatField(max_length=200, default=0);
	spots_remaining = models.IntegerField("Space Available", default=0);
'''
class Shelter_Form(ModelForm):
	class Meta:
		model = Shelter_Information
		fields = ['spots_remaining']
'''