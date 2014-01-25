from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
from social_secretary.ss_app.views import (
    fb_connect,
    set_contacts,
    fb_login_callback,
    redirect_signin_function,
    show_profile,
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
                       url(r'^/?$', RedirectView.as_view(url='/accounts/signin')),
                       url(r'^accounts/complete', show_profile),
                       url(r'^accounts/signin$', 'userena.views.signin', {'template_name': 'signin.html',
                                                                          'redirect_signin_function': redirect_signin_function}),
                       url(r'^accounts/signup$', 'userena.views.signup', {'success_url': '/accounts/complete'}),
                       url(r'^accounts/', include('userena.urls')),
                       )
