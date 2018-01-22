from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(
        r'^verifin/$',
        'django.contrib.auth.views.login',
        name='verifin',
        kwargs={'template_name': 'veriadmin/check.html'}
    ),
    url(
        r'^verifout/$',
        'django.contrib.auth.views.logout',
        name='verifout',
        kwargs={'next_page': '/'}
    ),
)
