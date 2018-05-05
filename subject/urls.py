from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'subject'

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', login, {'template_name': 'auth/login.html'}),
    url(r'^(?P<id>\d+)/$', views.subject_chapters, name='subject_chapters'),
]
