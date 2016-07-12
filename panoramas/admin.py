from django.contrib import admin
from panoramas.models import PanoramaStore


@admin.register(PanoramaStore)
class PanoramaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
