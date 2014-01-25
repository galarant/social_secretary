from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
from social_secretary.ss_app.views import (
    fb_connect,
    set_contacts,
    fb_login_callback,
    finish_user_flow,
)

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'social_secretary.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'fb_connect', fb_connect),
                       url(r'set_contacts', set_contacts),
                       url(r'fb_login_callback', fb_login_callback),
                       url(r'finish_user_flow', finish_user_flow),
                       url(r'^/?$', RedirectView.as_view(url='/accounts/signin')),
                       url(r'^accounts/signin/?$', 'userena.views.signin', {'template_name': 'signin.html'}),
                       url(r'^accounts/', include('userena.urls')),
                       )
