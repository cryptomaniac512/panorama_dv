# coding=utf-8

from __future__ import unicode_literals

from django.contrib import admin

from main.models import Features, Feedback, Services, Portfolio


@admin.register(Portfolio)
class PortfoliAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Services)
admin.site.register(Features)
admin.site.register(Feedback)
