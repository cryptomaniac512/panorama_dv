# coding=utf-8

from __future__ import unicode_literals

import os
import shutil
from zipfile import ZipFile, is_zipfile, BadZipFile

from django.conf import settings


def get_store_relative_path(store_dir_name, slug_str):
    """Возвращает относительный путь к хранилищу панорамы.

    :param store_dir_name: имя директории стора панорамы
    :type store_dir_name: str
    :param slug_str: slug/url панорамы
    :type slug_str: str
    :return: относительный путь к хранилищу
    :rtype: str

    """
    path = os.path.join(store_dir_name, slug_str)
    return path


def get_store_full_path(store_dir_name, slug_str):
    """Возвращает полный путь к хранилищу панорамы.

    :param store_dir_name: имя директории стора панорамы
    :type store_dir_name: str
    :param slug_str: slug/url панорамы
    :type slug_str: str
    :return: абсолютный путь к хранилищу
    :rtype: str

    """
    store_relative_path = get_store_relative_path(store_dir_name, slug_str)
    path = os.path.join(settings.MEDIA_ROOT, store_relative_path)
    return path


def get_store_url(store_dir_name, slug_str):
    """Возвращает url к хранилищу панорамы.

    :param store_dir_name: имя директории стора панорамы
    :type store_dir_name: str
    :param slug_str: slug/url панорамы
    :type slug_str: str
    :return: url к к хранилищу
    :rtype: str

    """
    store_relative_path = get_store_relative_path(store_dir_name, slug_str)
    url = '{}{}/'.format(settings.MEDIA_URL, store_relative_path)
    return url


def make_store_dir(store_dir_name, slug_str):
    """Создает директорию хранилища панорамы, если она не существует.

    :param store_dir_name: имя директории стора панорамы
    :type store_dir_name: str
    :param slug_str: slug/url панорамы
    :type slug_str: str

    """
    store_full_path = get_store_full_path(store_dir_name, slug_str)
    if not os.path.isdir(store_full_path):
        os.makedirs(store_full_path)


def clear_store(store_dir_name, slug_str):
    """Очищает директорию хранилища панорамы.

    :param store_dir_name: имя директории стора панорамы
    :type store_dir_name: str
    :param slug_str: slug/url панорамы
    :type slug_str: str

    """
    store_full_path = get_store_full_path(store_dir_name, slug_str)

    if not os.path.isdir(store_full_path):
        raise FileNotFoundError('Panorama store direcory does not exists!')

    shutil.rmtree(store_full_path)


def build_store(store_dir_name, slug_str, zipfile):
    """Распаковывает архив в хранилище панорамы.

    :param store_dir_name: имя директории стора панорамы
    :type store_dir_name: str
    :param slug_str: slug/url панорамы
    :type slug_str: str
    :param zipfile: объект zip-архива
    :type zipfile: zipfile.ZipFile

    """
    if not is_zipfile(zipfile):
        raise BadZipFile('Файл должен быть zip-архивом!')

    store_full_path = get_store_full_path(store_dir_name, slug_str)

    zipfile = ZipFile(zipfile)
    zipfile.extractall(path=store_full_path)

    def _get_store_dir(_path):
        """Рекурсивный поиск директории хранилища относительно файла
        index.xml

        """
        for root, dirs, files in os.walk(_path):
            if 'index.xml' in files:
            #     for d in dirs:
            #         _get_store_dir(os.path.join(root, d))
            # else:
                return root

    _store_dir = _get_store_dir(store_full_path)

    _store_files = os.listdir(_store_dir)
    for item in _store_files:
        shutil.move(os.path.join(_store_dir, item),
                    store_full_path)

    shutil.rmtree(_store_dir)
