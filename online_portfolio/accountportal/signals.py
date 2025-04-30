# MODULES AND LIBRARIES 
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# MODELS
from .models import Profile



# SIGNALS

##############################

# REGISTER PAGE

##############################

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:

        profile = Profile.objects.create(user=instance)
        profile.customer_id = instance.username
        profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):

    instance.profile.save()