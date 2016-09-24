from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit/$', views.submit),
    url(r'show/(\d+)/$', views.show),
    url(r'login/(\w+)/$', views.login),
]
