# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Portfolio
from django.contrib.auth.models import Group

admin.site.register(Portfolio)
