from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^update/(?P<pk>[\-\w]+)/$', views.edit_user, name='update'),
    url(r'^profile/(?P<pk>[\-\w]+)/$', views.profile_user, name='profile'),
    url(r'^profilekine/(?P<pk>[\-\w]+)/$', views.profile_kine, name='profilekine'),
    url(r'^updatekine/(?P<pk>[\-\w]+)/$', views.edit_kine, name='updatekine'),
    url(r'^questionnaire/$', views.questionnaire, name='questionnaire'),
    url(
        r'^choice/$',
        'django.contrib.auth.views.login',
        name='choice',
        kwargs={'template_name': 'extra/choice.html'}
    ),
]
