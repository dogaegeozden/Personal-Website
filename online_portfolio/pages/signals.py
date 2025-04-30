# LIBRARIES AND MODULES
from django.db.models.signals import post_save
from django.dispatch import receiver

# MODELS
from datacenter.models import GlobalSubscription
from pages.models import ContactPageMessage



# SIGNALS

##############################

# CONTACT PAGE

##############################

@receiver(post_save, sender=ContactPageMessage)
def send_email_on_new_contact_message(sender, instance, created, **kwargs):

    if created:

        instance.send_emails() 



##############################

# UNSUBSCRIPTION LINKS

##############################

@receiver(post_save, sender=GlobalSubscription)
def create_unsubscribe_link_signal(sender, instance, created, **kwargs):

    if created:

        instance.create_unsubscribe_link(instance)