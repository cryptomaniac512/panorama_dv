from .apps import MainConfig


def get_portfolio_filter_from_request(request):
    """Функция получения параметра фильтрации портфолио по url из реквеста.

    :param request: объект реквеста
    :type request: django.core.handlers.wsgi.WSGIRequest
    :return: словарь для фильтрации портфолио
    :rtype: dict

    """
    if request.resolver_match.app_name != MainConfig.name:
        return None

    query_by_pattern = {
        'main': {'on_main': True},
        'services': {'on_services': True},
    }

    pattern = query_by_pattern.get(request.resolver_match.url_name, None)
    if not pattern:
        return None

    portfolio_filter = {'is_published': True}
    portfolio_filter.update(pattern)

    return portfolio_filter
