from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
from .models import Features, Services


def get_main_page(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail(is_saved=True)
            return HttpResponseRedirect(reverse('main:main'))
    else:
        features = Features.objects.all()
        services = Services.objects.all()
        form = FeedbackForm()
        return render(request, 'main/main.html', {
            'features': features,
            'services': services,
            'form': form,
        })


def get_services_page(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail(is_saved=True)
            return HttpResponseRedirect(reverse('main:services'))
    else:
        services = Services.objects.all()
        form = FeedbackForm()
        return render(request, 'main/services.html', {
            'services': services,
            'form': form,
        })


def feedback_submit(request):
    """View обработки формы обратной связи.

    :param request: объект реквеста
    :type request: django.core.handlers.wsgi.WSGIRequest

    """
    if 'HTTP_REFERER' in request.META:
        referer = request.META['HTTP_REFERER']
    else:
        referer = reverse('main:main')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail(is_saved=True)
            result_text = ('Ваше сообщение принято! '
                           'Мы ознакомимся с ним в ближайшее время')
            messages.add_message(request, messages.SUCCESS, result_text)

    return HttpResponseRedirect(referer)
