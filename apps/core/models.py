from django.db import models


class BaseContentModel(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
