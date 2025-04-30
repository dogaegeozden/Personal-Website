# MODULES AND LIBRARIES
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.translation import get_language

# MODELS
from accountportal.models import (
    Profile,
)

# SETTINGS
from Online_Portfolio.settings import (
    YES_OR_NO_CHOICES,
    EMAIL_HOST_USER,
)



# DATA CLASSES

##############################

# GLOBAL MODELS

##############################

class GlobalPageVisit(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=False, null=False, verbose_name="Visit Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)
    page_url = models.URLField(max_length=2000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Page Visits'
        ordering = ['-visit_time']

class GlobalDocumentClickCoordinate(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=False, null=False, verbose_name="Click Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)
    x_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="X Coordinate",)
    y_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="Y Coordinate",)
    page_url = models.URLField(max_length=2000, null=True, blank=True, verbose_name="URL",)
    
    class Meta:
        
        verbose_name_plural = 'Global Document Click Coordinates'
        ordering = ['-click_time']

class GlobalMouseTrace(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    movement_time = models.DateTimeField(blank=False, null=False, verbose_name="Movement Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)
    x_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="X Coordinate",)
    y_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="Y Coordinate",)
    page_url = models.URLField(max_length=2000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Mouse Traces'
        ordering = ['-movement_time']

class GlobalKeystroke(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    pressing_time = models.DateTimeField(blank=False, null=False, verbose_name="Pressing Time", default=timezone.now,)
    keystroke = models.CharField(max_length=10, null=True, blank=True, verbose_name="Keystroke", default="N/A",)
    page_url = models.URLField(max_length=2000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Keystrokes'
        ordering = ['-pressing_time']

class GlobalSocialMediaButtonClick(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    platform_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Platform Choice",)
    click_time = models.DateTimeField(blank=False, null=False, verbose_name="Click Time", default=timezone.now,)
    page_url = models.URLField(max_length=2000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Social Media Button Clicks'
        ordering = ['-click_time']

class GlobalSubscription(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=150, verbose_name="email",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=1000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    subscribing_time = models.DateTimeField(blank=False, null=False, verbose_name="Subscribe Time", default=timezone.now,)
    
    def __str__(self):
    
        return self.email

    def create_unsubscribe_link(self, subscription):

        token = uuid4()
        GlobalUnsubscribeLink.objects.create(subscription=subscription, token=token)

    def get_unsubscribe_link(self):

        lang = get_language()
        unsubscribe_link = GlobalUnsubscribeLink.objects.get(subscription=self)

        if lang == "tr":
    
            return reverse("unsubscribe-translated", kwargs={"token": str(unsubscribe_link.token)})
    
        return reverse("unsubscribe", kwargs={"token": str(unsubscribe_link.token)})

    class Meta:

        verbose_name_plural = "Global Subscriptions"
        ordering = ['-subscribing_time']

class GlobalUnsubscribeLink(models.Model):

    subscription = models.OneToOneField(GlobalSubscription, on_delete=models.CASCADE,)
    token = models.CharField(max_length=255, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
    
        return self.subscription.email

    class Meta:

        verbose_name_plural = "Global Unsubscription Links"
        ordering = ['-created_at']

class GlobalAppDownloadButtonClick(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    app_choice = models.URLField(max_length=2000, null=False, blank=False, verbose_name="App Choice", default="N/A",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=1000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=False, null=False, verbose_name="Click Time", default=timezone.now,)

    class Meta:

        verbose_name_plural = 'Global App Download Button Clicks'
        ordering = ['-click_time']