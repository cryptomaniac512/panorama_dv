from django.db import models

from main.models import BaseContentModel


class PanoramaStore(BaseContentModel):
    store_dir_name = 'panorama_store'

    slug = models.SlugField('URL', max_length=20, unique=True)
    store_path = models.CharField('Относительный путь к хранилищу', null=False,
                                  unique=True, editable=False, max_length=200)

    class Meta:
        verbose_name = 'панорама'
        verbose_name_plural = 'панорамы'
