from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
from .models import Features, Services, Portfolio


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
        portfolio = Portfolio.objects.filter(
            is_published=True, on_services=True
        ).order_by('-pub_date')[:4]
        services = Services.objects.all()
        form = FeedbackForm()
        return render(request, 'website/content_pages/services.html', {
            'portfolio': portfolio,
            'services': services,
            'form': form,
        })
