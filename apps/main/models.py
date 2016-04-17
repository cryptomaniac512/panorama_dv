from django.db import models

# Create your models here.


class Feature(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'особенность'
        verbose_name_plural = 'особенности'
