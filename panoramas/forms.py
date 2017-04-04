from django import forms

from .models import PanoramaStore


class PanoramaAdminForm(forms.ModelForm):

    zipfile = forms.FileField(label='Архив для обработки', required=False)

    def save(self, commit=True):
        self.instance.zipfile = self.cleaned_data.get('zipfile', None)
        return super(PanoramaAdminForm, self).save(commit=commit)

    class Meta:
        model = PanoramaStore
        fields = '__all__'
