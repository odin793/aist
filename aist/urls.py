from django.conf.urls import patterns, include, url
from aist_app.views import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index_page, name="index_url"),
    url(r'^contacts/$', contacts, name="contacts"),
    url(r'^about/$', about, name="about"),
    url(r'^services/$', services, name="services"),
    url(r'^news/$', news_page, name="news"),
    url(r'^news/(\d+)/$', exact_new, name="exact_new"),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )