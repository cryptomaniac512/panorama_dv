from django.contrib import admin

from .forms import PanoramaAdminForm
from .models import PanoramaStore
from .processors import PanoramaStoreProcessor


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
            store = PanoramaStoreProcessor.make_from_zip(zipfile, obj)
            obj.store_path = store.relative_path

        obj.save()
