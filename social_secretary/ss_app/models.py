from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    rank = models.PositiveIntegerField()
    facebook_id = models.BigIntegerField(db_index=True)
    picture = models.ImageField(upload_to='/images')
    user = models.ForeignKey(User)


class FBUserInfo(models.Model):
    user = models.OneToOneField(User)
    facebook_id = models.BigIntegerField(db_index=True)
    oauth_token = models.CharField(max_length=512)
