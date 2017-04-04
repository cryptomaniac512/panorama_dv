# coding=utf-8

from __future__ import unicode_literals

from django.contrib import admin

from .forms import ServicesAdminForm, PortfolioAdminForm
from .models import Features, Feedback, Services, Portfolio


@admin.register(Portfolio)
class PortfoliAdmin(admin.ModelAdmin):

    form = PortfolioAdminForm
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):

    form = ServicesAdminForm


admin.site.register(Features)
admin.site.register(Feedback)
