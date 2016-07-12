import os
from uuid import uuid4

from django.core.urlresolvers import reverse
from django.db import models


class BaseContentModel(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Features(BaseContentModel):

    class Meta:
        verbose_name = 'особенность'
        verbose_name_plural = 'особенности'


class Services(BaseContentModel):

    def _get_path_and_rename_file(self, filename):
        """
            Возвращает путь и новое имя файла

            :param filename: текущее имя файла
            :type filename: str
            :return: строка относительного пути к файлу
            :rtype: str
        """
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join('services', filename)

    # TODO: Все SEO-плюшки вынести в миксин
    short_description = models.TextField('Краткое описание')
    image = models.ImageField(
        'Изображение', null=True,
        upload_to=_get_path_and_rename_file)

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'


class Portfolio(BaseContentModel):
    short_description = models.TextField('Краткое описание')
    image = models.ImageField('Превью', upload_to='portfolio/%Y/%m/%d')
    slug = models.SlugField('URL', max_length=40, unique=True)
    pub_date = models.DateTimeField('Дата публикации')
    is_published = models.BooleanField('Опубликовать', default=True)
    on_main = models.BooleanField('Показывать на главной', default=False)
    on_services = models.BooleanField(
        'Показывать на странице услуг', default=False)
    panorama_url = models.URLField('URL на панораму', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'портфолио'
        verbose_name_plural = 'портфолио'


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email', blank=True, null=True)
    phone = models.CharField('Контакнтый номер', max_length=20)
    service = models.ForeignKey(Services, blank=True, null=True,
                                verbose_name='Интересующая услуга')
    message = models.TextField('Сообщение')

    def __str__(self):
        return "{} ({})".format(self.name, self.phone)

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = verbose_name

    def get_edit_link(self):
        # TODO: Возможно, стоит это исправить на динамическое получение
        # имени приложения и модуля
        # TODO: Возможно, стоит вынести подобную функцию в иное место,
        # типа api
        return reverse('admin:main_feedback_change', args=(self.pk, ))
