import os
import shutil
from zipfile import BadZipFile, ZipFile, is_zipfile

from django.conf import settings
from django.db import models


class PanoramaStore(models.Model):
    store_dir_name = 'panorama_store'

    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField(max_length=20, unique=True, verbose_name='URL')

    def __init__(self, *args, **kwargs):
        super(PanoramaStore, self).__init__(*args, **kwargs)

        self._zipfile = None
        """Файл архива панорамы"""

    @staticmethod
    def _check_is_zip(zipfile):
        """Проверяет, что zipfile является архивом."""
        if not is_zipfile(zipfile):
            raise BadZipFile('Файл должен быть zip-архивом!')

    def _get_zipfile(self):
        """Возвращает файл архива из атрибута инстанса.

        :rtype zipfile: zipfile.ZipFile

        """
        return self._zipfile

    def _set_zipfile(self, zipfile):
        """Устанавливает файл архива в атрибут инстанса.

        :type zipfile: zipfile.ZipFile

        """
        self._check_is_zip(zipfile)
        self._zipfile = zipfile

    zipfile = property(_get_zipfile, _set_zipfile)
    """Property для работы с файлом архива панорамы через атрибут инстанса."""

    @property
    def absolute_path(self):
        """Возвращает абсолютный путь к хранилищу панорамы.

        :rtype: str

        """
        return os.path.join(settings.MEDIA_ROOT, self.store_dir_name, str(self.id))

    def build_store(self):
        """Выполняет сборку хранилища панорамы из переданного архива."""
        self._check_is_zip(self.zipfile)

        if os.path.isdir(self.absolute_path):
            shutil.rmtree(self.absolute_path)
        os.makedirs(self.absolute_path)

        zipfile = ZipFile(self.zipfile)
        zipfile.extractall(path=self.absolute_path)

    def save(self, *args, **kwargs):
        super(PanoramaStore, self).save(*args, **kwargs)

        if self.zipfile:
            self.build_store()

    def delete(self, *args, **kwargs):
        absolute_path = self.absolute_path
        super(PanoramaStore, self).delete(*args, **kwargs)
        shutil.rmtree(absolute_path)

    class Meta:
        verbose_name = 'панорама'
        verbose_name_plural = 'панорамы'
