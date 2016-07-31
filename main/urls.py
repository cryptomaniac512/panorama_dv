from django.conf.urls import url
from main import views


app_name = 'main'

urlpatterns = [
    url(r'^$', views.get_main_page, name='main'),
    url(r'^services/$', views.get_services_page, name='services'),
    url(r'^portfolios/$', views.get_portfolios_page, name='portfolios'),
    url(r'^portfolio/(?P<pk>[0-9]+)/$', views.get_portfolio_page,
        name='portfolio'),
    url(r'^feedback/$', views.feedback_submit, name='feedback'),
]
