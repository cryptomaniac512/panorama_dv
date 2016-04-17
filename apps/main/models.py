from django.db import models

from apps.core.models import BaseContentModel

# Create your models here.


class Feature(BaseContentModel):
    class Meta:
        verbose_name = 'особенность'
        verbose_name_plural = 'особенности'


class Services(BaseContentModel):
    short_description = models.TextField(
        'Краткое описание',
        help_text='Для главной страницы и SEO'
    )

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
