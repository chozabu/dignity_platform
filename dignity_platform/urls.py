
__author__ = "Alex 'Chozabu' P-B"
__copyright__ = "Copyright 2016, Chozabu"

from django.conf.urls import url
from django.conf.urls.static import static

import dignity.settings as settings

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

theme_dir = settings.BASE_DIR + "/startbootstrap-creative-1.0.2"


urlpatterns += static("/css/", document_root=theme_dir + "/css")
urlpatterns += static("/fonts/", document_root=theme_dir + "/fonts")
urlpatterns += static("/img/", document_root=theme_dir + "/img")
urlpatterns += static("/js/", document_root=theme_dir + "/js")
urlpatterns += static("/less/", document_root=theme_dir + "/less")
urlpatterns += static("/font-awesome/", document_root=theme_dir + "/font-awesome")
