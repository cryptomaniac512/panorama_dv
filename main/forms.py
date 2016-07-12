# coding=utf-8

from __future__ import unicode_literals

from froala_editor.widgets import FroalaEditor

from django.conf import settings
from django.core.mail import send_mail
from django import forms

from .models import Feedback, Services


class FeedbackForm(forms.ModelForm):

    def send_mail(self, is_saved=False):
        if self.is_valid():
            name, email, phone, service, message = [
                self.cleaned_data.get(k) for k in [
                    'name', 'email', 'phone', 'service', 'message']]

            subj = "Новое сообщение от {}".format(name)
            body = "{} относительно услуги {}:\n\n" \
                   "{}\n\n" \
                   "Контакты отправителя: {}; {}".format(
                       subj, service, message, email, phone)

            if is_saved:
                body += "\n\nПросмотреть: http://panorama-dv.ru{0}".format(
                    self.instance.get_edit_link())

            send_mail(subj, body, settings.EMAIL_FROM, settings.EMAIL_TO)
            return True
        else:
            return False

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'required': True, 'placeholder': 'Имя:'
            }),
            'email': forms.EmailInput(attrs={
                'required': False, 'placeholder': 'Email:'
            }),
            'phone': forms.TextInput(attrs={
                'required': True, 'placeholder': 'Контактный номер:'
            }),
            'service': forms.Select(attrs={
                'required': False,
            }),
            'message': forms.Textarea(attrs={
                'required': True, 'rows': 6, 'placeholder': 'Сообщение'
            }),
        }


class ServicesAdminForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        widgets = {
            'description': FroalaEditor(options={
                'height': 200, 'placeholderText': 'Подробное описание',
            }),
            'short_description': FroalaEditor(options={
                'height': 200, 'placeholderText': 'Для главной страницы и SEO',
            }),
        }
