from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm, TextInput, EmailInput, Select, Textarea
from .models import Feedback


class FeedbackForm(ModelForm):

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
            'name': TextInput(attrs={
                'required': True, 'placeholder': 'Имя:'
            }),
            'email': EmailInput(attrs={
                'required': False, 'placeholder': 'Email:'
            }),
            'phone': TextInput(attrs={
                'required': True, 'placeholder': 'Контактный номер:'
            }),
            'service': Select(attrs={
                'required': False,
            }),
            'message': Textarea(attrs={
                'required': True, 'rows': 6, 'placeholder': 'Сообщение'
            }),
        }
