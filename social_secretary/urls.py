from django.conf.urls import patterns, include, url

from django.contrib import admin
from social_secretary.ss_app.views import (
    fb_connect,
    set_contacts,
)

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'social_secretary.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'fb_connect', fb_connect),
                       url(r'set_contacts', set_contacts),
                       )
