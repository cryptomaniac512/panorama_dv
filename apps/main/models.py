from apps.core.models import BaseContentModel

# Create your models here.


class Feature(BaseContentModel):
    class Meta:
        verbose_name = 'особенность'
        verbose_name_plural = 'особенности'
