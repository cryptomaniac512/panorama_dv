# coding=utf-8

from django import forms

from .models import PanoramaStore


class PanoramaAdminForm(forms.ModelForm):

    zip_file_field = forms.FileField(label='Архив для обработки',
                                     required=False)

    def save(self, commit=True):
        zip_file_field = self.cleaned_data.get('zip_file_field', None)
        return super(PanoramaAdminForm, self).save(commit=commit)

    class Meta:
        model = PanoramaStore
        fields = '__all__'
