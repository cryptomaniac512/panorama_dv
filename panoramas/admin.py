from django.contrib import admin
from .models import PanoramaStore


@admin.register(PanoramaStore)
class PanoramaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
