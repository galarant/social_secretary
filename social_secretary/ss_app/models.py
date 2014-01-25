from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	facebook_id = models.BigIntegerField(db_index=True)

	def create_profile(sender, instance, created, **kwargs):
		if created:
			profile, created = UserProfile.objects.get_or_create(user=instance)

	post_save.connect(create_profile, sender=User)

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


#naive_calculate_score:
#	for each Interactions:
#		if (interaction.User = user && interaction.Contact = contact):
#			total = total + 1;

