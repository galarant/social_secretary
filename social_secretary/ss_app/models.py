from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacts(models.Model):
	name = models.CharField(max_length=255)
	facebook_id = models.BigIntegerField(db_index=True)
	picture = models.ImageField(upload_to='/images')



class Interactions(models.Model):
	contact = models.ForeignKey(Contacts);
	user = models.ForeignKey(User);
	interaction_type = models.CharField(max_length=255)
	interaction_dir = models.BinaryField() #0=U->C, 1=U<-C
	interaction_time = models.TimeField()




