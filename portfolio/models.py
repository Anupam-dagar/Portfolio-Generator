# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.conf import settings
class Portfolio(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200, blank=True)
	date_of_birth = models.DateField()
	email_address = models.EmailField(max_length=254)
	phone_number = models.SmallIntegerField(default="")
	small_bio = models.CharField(max_length=200, default="",blank=True)
	main_bio = models.CharField(max_length=600, default="", blank=True)
	skill1 = models.CharField(max_length=100, default="", blank=True)
	skill2 = models.CharField(max_length=100, default="", blank=True)
	skill3 = models.CharField(max_length=100, default="", blank=True)
	skill4 = models.CharField(max_length=100, default="", blank=True)
	skill5 = models.CharField(max_length=100, default="", blank=True)
	skill6 = models.CharField(max_length=100, default="", blank=True)
	def __str__(self):
		return self.first_name
	