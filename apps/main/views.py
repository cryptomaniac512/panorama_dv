from django.shortcuts import render
from .models import Features, Services


def get_main_page(request):
    features = Features.objects.all()
    services = Services.objects.all()
    return render(request, 'main/main.html', {
        'features': features,
        'services': services,
    })
