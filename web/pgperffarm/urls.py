"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    # Static pages
    url(r'^$', 'pgperffarm.views.index', name='index'),
    url(r'^/licence$', 'pgperffarm.views.licence', name='licence'),
    url(r'^/ppolicy$', 'pgperffarm.views.ppolicy', name='ppolicy'),

    # Auth system integration
    url(r'^(?:account/)?login/?$', 'pgperffarm.auth.login'),
    url(r'^(?:account/)?logout/?$', 'pgperffarm.auth.logout'),
    url(r'^auth_receive/$', 'pgperffarm.auth.auth_receive'),

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # This should not happen in production - serve with lightty!
    url(r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': '/static',
    }),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico',
                                                permanent=True))
]