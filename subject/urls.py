from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'subject'

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', login, {'template_name': 'auth/login.html'}),
    url(r'^(?P<id>\d+)(?P<subject_slug>[-\w]+)/$', views.subject_chapters, name='subject_chapters'),
]
