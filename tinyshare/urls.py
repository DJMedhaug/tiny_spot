from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', 'tiny_app.views.home', name='home'),
    url(r'^contact/$', 'tiny_app.views.contact', name='contact'),
    url(r'^about/$', 'tinyshare.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    # Django Registration Redux
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^forums/', include('forums.urls', namespace='forums')),
    url(r'^$', 'tiny_app.views.post_list', name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'tiny_app.views.post_detail', name='post_detail'),
    url(r'^post/new/$', 'tiny_app.views.post_new', name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'tiny_app.views.post_edit', name='post_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
