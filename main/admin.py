from django.contrib import admin

from .forms import PortfolioAdminForm, ServicesAdminForm
from .models import Features, Feedback, Portfolio, Services


@admin.register(Portfolio)
class PortfoliAdmin(admin.ModelAdmin):

    form = PortfolioAdminForm
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):

    form = ServicesAdminForm


admin.site.register(Features)
admin.site.register(Feedback)
