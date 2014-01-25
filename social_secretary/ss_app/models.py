from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    facebook_id = models.BigIntegerField(db_index=True)

    def image_url(self):
        return "http://graph.facebook.com/%s/picture" % self.facebook_id


class Ranking(models.Model):
    user = models.ForeignKey(User)
    contact = models.ForeignKey(Contacts)
    rank = models.PositiveIntegerField(null=True)


class FBUserInfo(models.Model):
    user = models.OneToOneField(User)
    facebook_id = models.BigIntegerField(db_index=True)
    oauth_token = models.CharField(max_length=512)
