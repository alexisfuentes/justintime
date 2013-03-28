from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
	'principal.views',
	url(r'^$', 'view_index', name='vista_index'),
	url(r'^login/$', 'view_login', name='vista_login'),
)