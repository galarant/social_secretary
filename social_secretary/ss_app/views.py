import json
from django.shortcuts import render
from django.http import HttpResponse

from models import Contact

from facepy import (
    GraphAPI,
    utils,
)

from social_secretary.settings import (
    FACEBOOK_APP_ID as app_id,
    FACEBOOK_APP_SECRET as app_secret,
)

from models import FBUserInfo


def fb_connect(request):
    return render(request, 'fb_connect.html')


def set_contacts(request):
    return render(request, 'set_contacts.html')


def redirect_signin_function(x, y):
    return "/accounts/complete"


def show_profile(request):
    return render(request, 'profile.html')


def fb_login_callback(request):
    creds = request.META['QUERY_STRING'].split('&')
    fbtoken = creds[0].split('=')[1]
    fb_usrid = creds[1].split('=')[1]
    extoken = utils.get_extended_access_token(fbtoken, app_id, app_secret)
    user = FBUserInfo(facebook_id=fb_usrid, oauth_token=extoken)
    # TODO fbtoken works, but extoken does not--why?
    graph = GraphAPI(fbtoken)
    paginator = graph.get('me/posts?fields=likes', page=True)

    # sort out the favorites
    counter = {}
    candidates = []
    while len(candidates) < 20:
        posts = paginator.next()['data']
        for post in posts:
            if 'likes' in post:
                likes = post['likes']['data']
                for like in likes:
                    person = (int(like['id']), like['name'])
                    if person in counter:
                        counter[person] += 1
                        if counter[person] == 3:
                            candidates.append(person)
                    else:
                        counter[person] = 1

    temp_list = []

    for person in candidates:
        contact = Contact(facebook_id=person[0], name=person[1])
        img_url = contact.image_url()

        contact.save

        facebook_id = contact.facebook_id
        facebook_name = contact.name
        temp_list.append((facebook_id, img_url, facebook_name))

    json_list = json.dumps(temp_list)

    return HttpResponse(json_list, content_type="application/json")
