import os

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.static import serve

from .models import PanoramaStore


def get_panorama_page(request, slug=None):
    try:
        panorama = PanoramaStore.objects.get(slug=slug)
    except PanoramaStore.DoesNotExist:
        return HttpResponseRedirect(reverse('main:main'))

    return render(request, panorama)


def get_panorama_static(request, slug, static):
    try:
        panorama = PanoramaStore.objects.get(slug=slug)
    except PanoramaStore.DoesNotExist:
        return HttpResponseRedirect(reverse('main:main'))

    filepath = os.path.join(panorama.absolute_path, static)
    return serve(request, os.path.basename(filepath),
                 os.path.dirname(filepath))
