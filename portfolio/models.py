# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.conf import settings
import datetime
class Portfolio(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200, blank=True)
	date_of_birth = models.DateField()
	email_address = models.EmailField(max_length=254)
	phone_number = models.BigIntegerField(default=None)
	small_bio = models.CharField(max_length=200, default="", blank=True)
	main_bio = models.CharField(max_length=600, default="")
	skill1 = models.CharField(max_length=100, default="")
	skill2 = models.CharField(max_length=100, default="")
	skill3 = models.CharField(max_length=100, default="", blank=True)
	skill4 = models.CharField(max_length=100, default="", blank=True)
	skill5 = models.CharField(max_length=100, default="", blank=True)
	skill6 = models.CharField(max_length=100, default="", blank=True)
	facebook =  models.CharField(max_length=500, default="")
	github = models.CharField(max_length=500, default="", blank=True)
	twitter = models.CharField(max_length=500, default="", blank=True)
	linkedin = models.CharField(max_length=500, default="", blank=True)
	blog = models.CharField(max_length=500, default="", blank=True)
	project1_name = models.CharField(max_length=500, default="", blank=True)
	project1_url = models.CharField(max_length=500, default="", blank=True)
	project1_description = models.CharField(max_length=300, default="", blank=True)
	project2_name = models.CharField(max_length=500, default="", blank=True)
	project2_url = models.CharField(max_length=500, default="", blank=True)
	project2_description = models.CharField(max_length=300, default="", blank=True)	
	project3_name = models.CharField(max_length=500, default="", blank=True)
	project3_url = models.CharField(max_length=500, default="", blank=True)
	project3_description = models.CharField(max_length=300, default="", blank=True)
	date_created = models.DateField(auto_now_add=True)
	time_created = models.TimeField(auto_now_add=True)
	updated_on = models.DateField(auto_now=True)
	updated_at = models.TimeField(auto_now=True)

	def __str__(self):
		return self.first_name	+ " " + self.last_name

class Feedback(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	feedback_field = models.CharField(max_length=1500,blank=True)
	feedback_done = models.BooleanField(default=False)

	def save(self):
		if self.feedback_done == False:
			self.feedback_done = True
		super(Feedback, self).save()

	def __str__(self):
		return str(self.pk) + " - " + self.user.username
