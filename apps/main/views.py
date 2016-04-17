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
