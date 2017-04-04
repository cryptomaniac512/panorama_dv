from django.contrib import admin

from .forms import PanoramaAdminForm
from .models import PanoramaStore


@admin.register(PanoramaStore)
class PanoramaAdmin(admin.ModelAdmin):

    form = PanoramaAdminForm

    prepopulated_fields = {'slug': ('title', )}
