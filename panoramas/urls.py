from django.conf.urls import url

from . import views

app_name = 'panoramas'

urlpatterns = [
    url(r'^(?P<slug>[^\.]+?)\/(?P<static>.+)', views.get_panorama_static,
        name='panorama_page'),
    url(r'^(?P<slug>[^\.]+?)\/', views.get_panorama_page,
        name='panorama_static'),
]
