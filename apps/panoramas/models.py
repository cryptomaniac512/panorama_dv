import os
import shutil
from zipfile import ZipFile, is_zipfile, BadZipFile

from django.conf.global_settings import MEDIA_ROOT
from django.db import models

from main.models import BaseContentModel


class PanoramaStore(BaseContentModel):
    store_dir_name = 'panorama_store'

    slug = models.SlugField('URL', max_length=20, unique=True)
    store_path = models.CharField('Относительный путь к хранилищу', null=False,
                                  unique=True, editable=False, max_length=200)
    zip_file = models.FileField('Архив для обработки', null=True, blank=True)

    def __store_full_path(self):
        """Возвращает полный путь к хранилищу панорамы, каким он должен быть.

        """
        path = os.path.join(MEDIA_ROOT, self.store_dir_name, self.slug)
        return path

    @property
    def store_full_path(self):
        """Возвращает полный путь к хранилищу панорамы, если он существует.

        :return: абсолютный путь к хранилищу
        :rtype: str

        """
        path = self.__store_full_path()
        if os.path.isdir(path):
            return path

    def mkdir(self):
        """Создает директорию хранилища панорамы, если она не существует.

        """
        if not self.store_full_path:
            path = self.__store_full_path()
            os.makedirs(path)

    def _remove_store(self):
        """Очищает директорию хранилища панорамы.

        """
        if not self.store_full_path:
            raise FileNotFoundError('Panorama store direcory does not exists!')
        shutil.rmtree(self.store_full_path)

    def build_store(self, zipfile):
        """Распаковывает архив в хранилище панорамы.

        :param zipfile: объект zip-архива
        :type zipfile: zipfile.ZipFile
        :return: результат распаковки
        :rtype: bool

        """
        if is_zipfile(zipfile):
            zipfile = ZipFile(zipfile)
            zipfile.extractall(path=self.store_full_path)

            def _get_store_dir(_path):
                for root, dirs, files in os.walk(_path):
                    if 'index.xml' not in files:
                        for d in dirs:
                            _get_store_dir(os.path.join(root, d))
                    else:
                        return root

            _store_dir = _get_store_dir(self.store_full_path)
            _store_files = os.listdir(_store_dir)
            for item in _store_files:
                shutil.move(os.path.join(_store_dir, item),
                            self.store_full_path)
            shutil.rmtree(_store_dir)
        else:
            raise BadZipFile('Файл должен быть zip-архивом!')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.zip_file:
            if not self.store_full_path:
                self.mkdir()
            else:
                self._remove_store()
                self.mkdir()
            self.build_store(self.zip_file)
            self.store_path = self.store_full_path
            self.zip_file = None

        return super(PanoramaStore, self).save(
           force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'панорама'
        verbose_name_plural = 'панорамы'
