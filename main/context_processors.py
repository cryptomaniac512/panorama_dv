from .api import get_portfolio_filter_from_request
from .forms import FeedbackForm
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


def get_feedback_form(request):
    """Контекст-процессор для получения печатной формы.

    :param request: объект реквеста
    :type request: django.core.handlers.wsgi.WSGIRequest

    """
    form = FeedbackForm()
    return {
        'g_feedback_form': form,
    }
