# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Portfolio, Feedback

class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'time_created', 'updated_on', 'updated_at')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Feedback)