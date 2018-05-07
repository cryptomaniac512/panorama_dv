from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^panoramas/', include('panoramas.urls')),
]

# Serve media and statis if DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
