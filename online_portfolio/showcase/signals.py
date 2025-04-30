# LIBRARIES AND MODULES
from django.db.models.signals import post_save
from django.dispatch import receiver

# MODELS
from .models import ProjectDetailPageFeedback



##############################

# PROJECTS PAGE

##############################

@receiver(post_save, sender=ProjectDetailPageFeedback)
def send_email_on_feedback(sender, instance, created, **kwargs):

    if created:

        instance.send_emails()
