from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'subject'

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'auth/logout.html'}, name='logout'),
    url(r'^(?P<id>\d+)/$', views.subject_chapters, name='subject_chapters'),
]
