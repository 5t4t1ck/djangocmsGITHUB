from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.assess_index, name='assess_index'),
    url(r'^save_message/$', views.save_message, name='assess_save_message'),
]
