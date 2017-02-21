import os

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
