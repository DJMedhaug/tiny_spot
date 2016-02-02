from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'tiny_app.views.post_list', name='home'),
    url(r'^contact/$', 'tiny_app.views.contact', name='contact'),
    url(r'^about/$', 'tinyshare.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # Django Registration Redux
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^forums/', include('forums.urls', namespace='forums')),
    url(r'^$', 'tiny_app.views.post_list', name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'tiny_app.views.post_detail', name='post_detail'),
    url(r'^post/new/$', 'tiny_app.views.post_new', name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'tiny_app.views.post_edit', name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', 'tiny_app.views.post_remove', name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', 'tiny_app.views.post_publish', name='post_publish'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)