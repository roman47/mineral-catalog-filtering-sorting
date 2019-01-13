from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'search/$', views.search, name='search'),
    url(r'single_letter/(?P<pk>\D+)/$', views.single_letter, name='single_letter'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    #url(r'^$', views.course_list, name='list'),
    #url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step'),,
    #url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]