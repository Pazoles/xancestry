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
from django.urls import path
from django.views.generic import RedirectView
import django.views.static
import django.contrib.auth.views
import os.path
import settings

urlpatterns = [
    url(r'', include('people.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/'}, name='logout'),
]

# Get Django to serve media files in debug mode.
if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$',
                        django.views.static.serve,
                        {'document_root': settings.MEDIA_ROOT})]

urlpatterns = [
    path('admin/', admin.site.urls),
]
