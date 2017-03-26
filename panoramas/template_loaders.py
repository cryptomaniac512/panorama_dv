import os.path

from django.template import Origin
from django.template.loaders.filesystem import Loader as BaseLoader

from .models import PanoramaStore


class Loader(BaseLoader):
    """Загрузчик шаблонов хранилища панорам."""

    TEMPLATE_NAME = 'index.html'

    def get_template_sources(self, panorama_obj):
        if isinstance(panorama_obj, PanoramaStore):
            yield Origin(
                name=os.path.join(
                    panorama_obj.absolute_path, self.TEMPLATE_NAME),
                template_name=self.TEMPLATE_NAME,
                loader=self,
            )
