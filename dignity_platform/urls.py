
__author__ = "Alex 'Chozabu' P-B"
__copyright__ = "Copyright 2016, Chozabu"

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^people/$', views.people, name='people'),
    url(r'^people/(?P<person_id>[0-9]+)/$', views.person, name='person'),
    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^jobs/(?P<job_id>[0-9]+)/$', views.job, name='job'),
    url(r'^causes/$', views.causes, name='causes'),
    url(r'^causes/(?P<cause_id>[0-9]+)/$', views.cause, name='cause'),
]