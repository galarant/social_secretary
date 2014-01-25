from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacts(models.Model):
	name = models.CharField(max_length=255)
	facebook_id = models.BigIntegerField(db_index=True)
	picture = models.ImageField(upload_to='/images')


class Ranking(models.Model):
    user = models.ForeignKey(User);
    contact = models.ForeignKey(Contacts);
    rank = models.PositiveIntegerField();
