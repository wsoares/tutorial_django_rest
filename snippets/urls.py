from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.snippet_list, name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
]