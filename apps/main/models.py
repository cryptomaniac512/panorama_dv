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
    short_description = models.TextField(
        'Краткое описание',
        help_text='Для главной страницы и SEO'
    )

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'


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
