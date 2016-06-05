from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from panoramas.models import PanoramaStore


def get_panorama_page(request, slug=None):
    panoramas = PanoramaStore.objects.filter(slug=slug).values_list(
        'store_path', flat=True)
    if not panoramas.exists():
        return HttpResponseRedirect(reverse('main:main'))
    else:
        return render(request, 'panoramas/index.html', {
            'store': panoramas.last(),
        })
