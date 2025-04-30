# LIBRARIES
from django.db import models
from PIL import Image
from uuid import uuid4
from django.core.mail import send_mail
from django.template.loader import render_to_string
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.translation import get_language

# ONLINE PORTFOLIO MODULES
from modules.validators import validate_file_size

# MODELS
from django.contrib.auth.models import User

# SETTINGS
from Online_Portfolio.settings import (
    COUNTRY_CHOICES,
    YES_OR_NO_CHOICES,
    EMAIL_HOST_USER,
)



# DATA CLASSES

##############################

# LOGIN PAGE

##############################

class LoginPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and that's why, "
                "you should use sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Login Page Meta Descriptions"



##############################

# LOGOUT PAGE

##############################

class LogoutPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False, 
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the "
                "page's content. Creating a meta description element is beneficial "
                "for better SEO and that's why, you should use sentences which will "
                "catch the user's attention."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Logout Page Meta Descriptions"



##############################

# REGISTER PAGE

##############################

class RegisterPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes "
                "the page's content. Creating a meta description element is "
                "beneficial for better SEO and that's why, you should use "
                "sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Register Page Meta Descriptions"



##############################

# PROFILE PAGE

##############################

class Profile(models.Model):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        verbose_name="Universal Unique Identifier", 
        help_text="Universal Unique Identifier",
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(verbose_name="Customer ID", unique=True, max_length=255, null=True, blank=True,)
    company_name = models.CharField(verbose_name="Company Name", unique=True, max_length=255, null=True, blank=True,)
    phone_number = PhoneNumberField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    date_of_birth = models.DateTimeField(blank=True, null=True, verbose_name="Date of Birth")
    
    def generate_profile_picture_upload_path(instance, field_attname):

        current_username = getattr(instance.user, 'username', 'default_username')

        return f'profiles/{current_username}/{field_attname}'

    image = models.ImageField(
        default='defaults/default_user_profile_picture.jpg',
        upload_to=generate_profile_picture_upload_path,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],
    )
    country = models.CharField(
        verbose_name="Country of Residence",
        help_text="Enter user's country of residence.",
        max_length=4,
        choices=COUNTRY_CHOICES,
        null=True,
        blank=True,
    )
    salesperson_uuid = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Sales Person's UUID",
        default="N/A",
    )
    salesperson_username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Sales Person's Username",
        default="N/A",
    )
    deliverables_password = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Deliverables Password",
    )
    alternative_email_1 = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Alternative Email 1",
    )
    alternative_email_2 = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Alternative Email 2",
    )
    alternative_email_3 = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Alternative Email 3",
    )
    alternative_email_4 = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Alternative Email 4",
    )
    alternative_email_5 = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Alternative Email 5",
    )
    alternative_email_last = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Last Alternative Email",
    )

    def __str__(self):

        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        To edit profile pictures before saving.
        Scales the image to a maximum of 300x300 pixels if it exceeds these dimensions.
        """

        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:

            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        
        verbose_name_plural = "Profile Page Profiles"



##############################

# PASSWORD RESET COMPLETE PAGE

##############################

class PasswordResetCompletePageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the "
                "page's content. Creating a meta description element is beneficial "
                "for better SEO and that's why, you should use sentences which will "
                "catch the user's attention."
            ),
        ),
    )

    class Meta:
        
        verbose_name_plural = "Password Reset Complete Page Meta Descriptions"
        # Shortened table name. 
        # Hint: You are providing a short name because, 
        # accountportal_passwordresetcompletepagemetadescription_translation 
        # is too long for mysql so, it's causing an error.
        db_table = "accountportal_pwdrcomppmd"



##############################

# PASSWORD RESET CONFIRM PAGE

##############################

class PasswordResetConfirmPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the "
                "page's content. Creating a meta description element is beneficial "
                "for better SEO and that's why, you should use sentences which will "
                "catch the user's attention."
            ),
        ),
    )

    class Meta:
        
        verbose_name_plural = "Password Reset Confirm Page Meta Descriptions"
        db_table = "accountportal_pwdrconfirmpmd"



##############################

# PASSWORD RESET DONE PAGE

##############################

class PasswordResetDonePageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and that's why, "
                "you should use sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:
        
        verbose_name_plural = "Password Reset Done Page Meta Descriptions"
        db_table = "accountportal_pwdrdonepmd"



##############################

# PASSWORD RESET FORM PAGE

##############################

class PasswordResetFormPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. Creating "
                "a meta description element is beneficial for better SEO and that's why, you "
                "should use sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:
        
        verbose_name_plural = "Password Reset Form Page Meta Descriptions"
        db_table = "accountportal_pwdrformpmd"



##############################

# ANNOUNCEMENTS PAGE

##############################

class AnnouncementsPageAnnouncement(TranslatableModel):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Creator",)
    translations = TranslatedFields(
        title = models.CharField(
            verbose_name="Title",
            max_length=250,
            null=False,
            blank=False,
            default="Lorem Ipsum",
        ),
        text = models.TextField(
            max_length=10000,
            null=False,
            blank=False,
            default=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
                "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
                "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo "
                "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum "
                "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
                "sunt in culpa qui officia deserunt mollit anim id est laborum."
            ),
        ),
    )
    create_time = models.DateTimeField(blank=False, null=False, verbose_name="Create Time", default=timezone.now,)
    visible_to_groups = models.ManyToManyField(Group, related_name='announcement_visible_to', blank=True,)

    def get_absolute_url(self):

        lang = get_language()
    
        if lang == "tr":
    
            return reverse("announcement-detail-translated", kwargs={"id": self.pk})
    
        return reverse("announcement-detail", kwargs={"id": self.pk})

    def __str__(self):

        return f'{self.title} - {self.id}'

    class Meta:

        verbose_name_plural = "Announcements Page Announcements"
        ordering = ['-create_time']

class AnnouncementsPageUserAnnouncementView(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="viewed_announcements")
    announcement = models.ForeignKey(AnnouncementsPageAnnouncement, on_delete=models.CASCADE, related_name="viewed_by")
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "Announcements Page User Announcement Views"
        ordering = ['-viewed_at']
