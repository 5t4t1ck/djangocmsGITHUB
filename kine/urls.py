from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register , name='register'),
    url(r'^registerpatient/$', views.registerpatient , name='registerpatient'),
    url(r'^patient/$', views.patient , name='patient'),
    url(r'^patientid/$', views.patientid , name='patientid'),
    url(r'^see/(?P<pk>[\-\w]+)/$', views.see, name='see'),
    url(r'^questionnaire/(?P<pk>[\-\w]+)/$', views.questionnaire, name='questionnaire'),
        url(r'^questionnaire/read/(?P<pk>[\-\w]+)/$', views.questionnaireread, name='questionnaireread'),
    url(
        r'^choice/$',
        'django.contrib.auth.views.login',
        name='choice',
        kwargs={'template_name': 'kine/choice.html'}
    ),
    url(
        r'^info/$',
        'django.contrib.auth.views.login',
        name='info',
        kwargs={'template_name': 'kine/info.html'}
    ),
]
