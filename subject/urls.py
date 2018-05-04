from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', login, {'template_name': 'auth/login.html'})
]
