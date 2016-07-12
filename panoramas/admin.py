import os

from django.contrib import admin

from .api import (
    get_store_full_path, clear_store, make_store_dir, build_store,
    get_store_relative_path)
from .forms import PanoramaAdminForm
from .models import PanoramaStore


@admin.register(PanoramaStore)
class PanoramaAdmin(admin.ModelAdmin):

    form = PanoramaAdminForm

    prepopulated_fields = {'slug': ('title', )}

    def save_model(self, request, obj, form, change):
        """Переопределенная логика сохранения инстанса модели.

        :param request: реквест
        :type request: django.core.handlers.wsgi.WSGIRequest
        :param obj: инстанс модели
        :type obj: panoramas.models.PanoramaStore
        :param form: форма с полями данных
        :type form: django.forms.widgets.PanoramaStoreForm
        :param change: признак, что это изменение инстанса
        :type change: bool

        """
        zipfile = form.cleaned_data.get('zip_file_field', None)

        if zipfile:

            store_dir_name = obj.store_dir_name
            slug_str = form.cleaned_data.get('slug')
            store_full_path = get_store_full_path(store_dir_name, slug_str)

            if not os.path.isdir(store_full_path):
                make_store_dir(store_dir_name, slug_str)
            else:
                clear_store(store_dir_name, slug_str)
                make_store_dir(store_dir_name, slug_str)

            build_store(store_dir_name, slug_str, zipfile)
            obj.store_path = get_store_relative_path(store_dir_name, slug_str)

        obj.save()
