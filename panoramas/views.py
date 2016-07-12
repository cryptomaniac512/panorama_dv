from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from panoramas.models import PanoramaStore


def get_panorama_page(request, slug=None):
    panoramas = PanoramaStore.objects.filter(slug=slug)
    if not panoramas.exists():
        return HttpResponseRedirect(reverse('main:main'))
    else:
        panorama = panoramas.last()
        return render(request, 'panoramas/index.html', {
            'store': panorama.store_url,
        })
