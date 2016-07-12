from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .api import get_store_url
from .models import PanoramaStore


def get_panorama_page(request, slug=None):
    panoramas = PanoramaStore.objects.filter(slug=slug)
    if not panoramas.exists():
        return HttpResponseRedirect(reverse('main:main'))
    else:
        panorama = panoramas.last()
        panorama_store_url = get_store_url(
            panorama.store_dir_name, panorama.slug)
        return render(request, 'panoramas/index.html', {
            'store': panorama_store_url,
        })
