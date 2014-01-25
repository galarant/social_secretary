from django.shortcuts import render
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


def fb_login_callback(request):
		creds = request.META['QUERY_STRING'].split('&')
		fbtoken = creds[0].split('=')[1]
		fb_usrid = creds[1].split('=')[1]
		extoken = utils.get_extended_access_token(fbtoken, app_id, app_secret)
		user = FBUserInfo(facebook_id = fb_usrid, oauth_token = extoken)
		#TODO fbtoken works, but extoken does not--why?
		graph = GraphAPI(fbtoken)
		paginator = graph.get('me/posts?fields=likes',page=True)

		#sort out the favorites
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
							counter[person]+=1
							if counter[person] == 3:
								candidates.append(person)
						else:
							counter[person]=1
		#now turn this into a JSON object

		#TODO template is not the right one
		return render(request, 'set_contacts.html')
