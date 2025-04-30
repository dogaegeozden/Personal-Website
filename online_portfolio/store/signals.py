# LIBRARIES AND MODULES
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# MODELS
from .models import (
    ServiceDetailPageServiceInquiry,
)



# SIGNALS

##############################

# SERVICES PAGE

##############################

@receiver(post_save, sender=ServiceDetailPageServiceInquiry)
def send_email_on_service_inquiry(sender, instance, created, **kwargs):

    if created:

        instance.send_emails()