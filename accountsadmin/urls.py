from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(
        r'^loginadmin/$',
        'django.contrib.auth.views.login',
        name='loginadmin',
        kwargs={'template_name': 'accountsadmin/loginadmin.html'}
    ),
    url(
        r'^logoutadmin/$',
        'django.contrib.auth.views.logout',
        name='logoutadmin',
        kwargs={'next_page': '/'}
    ),
    url(
        r'^password_change/$',
        'django.contrib.auth.views.password_change',
        name='password_change',
        kwargs={
               'template_name': 'accountsadmin/password_change_form.html',
               'post_change_redirect':'accountsadmin:password_change_done',
               }
    ),
    url(
        r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done',
        kwargs={'template_name': 'accountsadmin/password_change_done.html'}
    ),
)
