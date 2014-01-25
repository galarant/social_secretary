from django.shortcuts import render
from facepy import (
    GraphAPI,
    utils,
)

from social_secretary.settings import (
    FACEBOOK_APP_ID as app_id,
    FACEBOOK_APP_SECRET as app_secret,
)

def fb_connect(request):
    return render(request, 'fb_connect.html')


def set_contacts(request):
    return render(request, 'set_contacts.html')

def fb_login_callback(request):
    creds = request.META['QUERY_STRING'].split('&')
    fbtoken = creds[0].split('=')[1]
    fb_usrid = creds[1].split('=')[1]
    graph = GraphAPI(fbtoken)
    utils.get_extended_access_token(fbtoken, app_id, app_secret)
    return render(request, 'fb_login_request.html')
