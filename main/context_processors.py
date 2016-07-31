from .api import get_portfolio_filter_from_request
from .models import Portfolio


def get_portfolio(request):
    """Контекст-процессор для печати превью порлфолио.

    :param request: объект реквеста
    :type request: django.core.handlers.wsgi.WSGIRequest

    """
    query_filter = get_portfolio_filter_from_request(request)
    portfolios = []
    if query_filter:
        portfolios = Portfolio.objects.filter(**query_filter)
    return {
        'g_portfolio': portfolios,
    }
