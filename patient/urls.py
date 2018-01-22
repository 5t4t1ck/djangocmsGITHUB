# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accountsadmin/', include('accountsadmin.urls', namespace='accountsadmin')),
    url(r'^extra/', include('extra.urls', namespace='extra')),
    url(r'^practice/', include('practice.urls', namespace='practice')),
    url(r'^questionnaire/', include('questionnaire.urls', namespace='questionnaire')),
    url(r'^kine/', include('kine.urls', namespace='kine')),
    url(r'^veriadmin/', include('veriadmin.urls', namespace='veriadmin')),
    url(r'^assessment/', include('assessment.urls', namespace='assessment')),
    url(r'^postman/', include('postman.urls', namespace='postman')),

]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
