import os
import shutil
from zipfile import ZipFile, is_zipfile, BadZipFile

from django.conf import settings


class PanoramaStoreProcessor:
    """Класс процессинга панорам.

    Обслуживает создание хранилищ панорам и получение существующих.

    """

    def __init__(self, obj=None, force_make=False):
        """
        :param obj: инстанс хранилища панорам
        :type obj: .models.PanoramaStore
        :param force: начать производство/пересборку при инстанцировании
        :type force: bool

        """
        self.obj = obj

    @property
    def relative_path(self):
        """Возвращает относительный путь к хранилищу панорамы.

        :rtype: str

        """
        return os.path.join(self.obj.store_dir_name, self.obj.slug)

    @property
    def full_path(self):
        """Возвращает полный путь к хранилищу панорамы.

        :rtype: str

        """
        return os.path.join(settings.MEDIA_ROOT, self.relative_path)

    def _make_store_dir(self):
        """Создает директорию хранилища панорамы, если она не существует."""
        if not os.path.isdir(self.full_path):
            os.makedirs(self.full_path)

    def _clear_store(self):
        """Очищает директорию хранилища панорамы."""
        if not os.path.isdir(self.full_path):
            raise FileNotFoundError('Хранилище панорамы не существует!')

        shutil.rmtree(self.full_path)

    def _build_store(self, zipfile):
        """Процесс сборки хранилища панорамы из переданного архива.

        :param zipfile: архив файлов для производства панорамы
        :type zipfile: zipfile.ZipFile

        """
        if not is_zipfile(zipfile):
            raise BadZipFile('Файл должен быть zip-архивом!')

        zipfile = ZipFile(zipfile)
        zipfile.extractall(path=self.full_path)

        store_dir = self._get_setting_dir()

        for item in os.listdir(store_dir):
            shutil.move(os.path.join(store_dir, item), self.full_path)

        shutil.rmtree(store_dir)

    def _get_setting_dir(self):
        """Рекурсивный поиск директории хранилища относительно файла
        index.xml.

        :rtype: str

        """
        for root, dirs, files in os.walk(self.full_path):
            if 'index.xml' in files:
                return root

    @classmethod
    def make_from_zip(cls, zipfile, obj):
        """Создает новое хранилище панорамы из переданного архива для
        указанного объекта.

        :param zipfile: архив файлов для производства панорамы
        :type zipfile: zipfile.ZipFile
        :param obj: инстанс хранилища панорам
        :type obj: .models.PanoramaStore

        """
        obj = cls(obj=obj)
        obj._build_store(zipfile)
        return obj
