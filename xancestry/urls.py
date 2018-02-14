"""xancestry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
import django.views.static
import django.contrib.auth.views
import os.path
from . import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index, name='xancestry.index'),
    url(r'^person/(?P<person_id>\d+)/$', views.person, name='person'),
    url(r'^person/(?P<person_id>\d+)/edit/$', views.edit_person, name='edit_person'),
    url(r'^person/(?P<person_id>\d+)/relatives/$', views.relatives, name='relatives'),
    url(r'^person/(?P<person_id>\d+)/relatives/map/$', views.relatives_map, name='relatives_map'),
    url(r'^person/(?P<person_id>\d+)/descendants/$', views.descendants, name='descendants'),
    url(r'^person/(?P<person_id>\d+)/descendants/map/$', views.descendants_map, name='descendants_map'),
    url(r'^person/(?P<person_id>\d+)/descendants/tree/$', views.descendants_tree, name='descendants_tree'),
    url(r'^person/(?P<person_id>\d+)/descendants/tree/svg/$', views.descendants_tree_svg, name='descendants_tree_svg'),
    url(r'^person/(?P<person_id>\d+)/ancestors/$', views.ancestors, name='ancestors'),
    url(r'^person/(?P<person_id>\d+)/ancestors/report/$', views.ancestors_report, name='report'),
    url(r'^person/(?P<person_id>\d+)/ancestors/report/undead/$',
        views.ancestors_report_undead,
        name='report_undead'),
    url(r'^person/(?P<person_id>\d+)/ancestors/report/maiden-names/$',
        views.ancestors_report_maiden_names,
        name='report_maiden_names'),
    url(r'^report/alive/(?P<year>\d+)/$', views.alive_in_year, name='alive_in_year'),
    url(r'^person/(?P<person_id>\d+)/ancestors/map/$', views.ancestors_map, name='ancestors_map'),
    url(r'^person/(?P<person_id>\d+)/ancestors/ringchart/$', views.ring_chart, name='ring_chart'),
    url(r'^person/(?P<person_id>\d+)/ancestors/ringchart/svg/$', views.ring_chart_svg, name='ring_chart_svg'),
    url(r'^location/(?P<location_id>\d+)/$', views.location, name='location'),
    url(r'^region/(?P<region_name>[\w\W]+)/$', views.region, name='region'),
    url(r'^surname/(?P<surname>[\w\W]+)/$', views.surname, name='surname'),
    url(r'^forename/(?P<forename>[\w\W]+)/$', views.forename, name='forename'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag, name='tag'),
    url(r'^person/add/$', views.add_person, name='add_person'),
    url(r'^location/add/$', views.add_location, name='add_location'),

    url(r'^public/surnames/$', views.surnames, name='surnames'),
]

