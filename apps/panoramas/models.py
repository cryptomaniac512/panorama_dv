import os

from django.conf.global_settings import MEDIA_ROOT
from django.db import models

from apps.main.models import BaseContentModel


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

    def _clean_dir(self):
        """Очищает директорию хранилища панорамы.

        """
        if not self.store_full_path:
            raise FileNotFoundError('Panorama store direcory does not exists!')

        for root, dirs, files in os.walk(self.store_full_path):
            for f in files:
                os.remove(os.path.join(root, f))
            for d in dirs:
                os.remove(os.path.join(root, d))

    def extract_store(self, zipfile):
        """Распаковывает архив в хранилище панорамы.

        :param zipfile: объект zip-архива
        :type zipfile: zipfile.ZipFile
        :return: результат распаковки
        :rtype: bool

        """
        pass

    class Meta:
        verbose_name = 'панорама'
        verbose_name_plural = 'панорамы'
