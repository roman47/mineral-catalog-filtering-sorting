from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'search/$', views.search, name='search'),
    url(r'single_letter/(?P<pk>\D+)/$',
        views.single_letter, name='single_letter'),
    url(r'single_group/(?P<pk>\D+)/$',
        views.single_group, name='single_group'),
    url(r'single_color/(?P<pk>.*)/$',
        views.single_color, name='single_color')
]
