# MODULES AND LIBRARIES
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from django.template.loader import render_to_string
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# ONLINE PORTFOLIO MODULES
from modules.validators import validate_file_size

# SETTINGS
from Online_Portfolio.settings import (
    EMAIL_HOST_USER,
)



# DATA CLASSES

##############################

# HOME PAGE

##############################

class HomePageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            help_text=(
                "Meta description is an HTML element that describes the page's content. "
                "It is getting used for SEO so, you can use sentences that will catch the user's attention."
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Home Page Meta Descriptions"

class HomePageHeroSection(TranslatableModel):

    translation = TranslatedFields(
        title = models.CharField(max_length=250, blank=False, null=False, default="Lorem Ipsum"),
        image = models.ImageField(
            null=False,
            blank=False,
            default="assets/default.jpg",
            upload_to='home/hero_section',
            help_text=(
                "<strong>Note: </strong><li>Dimension requirement is 1.3 height/width</li>"
                "<li>Don't forget to scale down your images to increase load speed.</li>"
                "<li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change the file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        text = models.TextField(
            max_length=10000,
            blank=False,
            null=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "<strong>Notes: </strong><li>Introduce your self.</li>"
                "<li>Include the most relevant professional experience.</li>"
                "<li>Mention significant personal achievements or awards.</li>"
                "<li>Introduce personal details.</li><li>Use a casual and friendly tone.</li>"
            ),
        ),
        alt = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as '
                'it relates to the content of a document or webpage. It is read aloud '
                'to users by screen reader software, and it is indexed by search engines. '
                'It\'s good for better search engine optimization.'
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Home Page Hero Sections"

class HomePageProfilePicture(TranslatableModel):
    
    translation = TranslatedFields(
        image = models.ImageField(
            null=False,
            blank=False,
            default="assets/default.jpg",
            upload_to='home/profile_pictures',
            help_text=(
                "<strong>Note: </strong><li>Dimension requirement is 1.3 height/width</li>"
                "<li>Don't forget to scale down your images to increase load speed.</li>"
                "<li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change the file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size]
        ),
        alt = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            verbose_name="Alternative Text",
            default="Lorem Ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if a user "
                "for some reason cannot view it (because of slow connection, an error in "
                "the src attribute, or if the user uses a screen reader)."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Home Page Profile Pictures"

class HomePageBio(TranslatableModel):
    
    name = models.CharField(max_length=250, blank=False, null=False, default="Lorem Ipsum",)
    translation = TranslatedFields(
        text = models.TextField(
            max_length=10000,
            blank=False,
            null=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "<strong>Notes: </strong><li>Introduce your self.</li>"
                "<li>Include the most relevant professional experience.</li>"
                "<li>Mention significant personal achievements or awards.</li>"
                "<li>Introduce personal details.</li><li>Use a casual and friendly tone.</li>"
            ),
        ),
    )
    
    class Meta:

        verbose_name_plural = "Home Page Bios"

class HomePageToolOrLanguage(models.Model):
    
    title = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        default="Lorem Ipsum",
        help_text="Create a title for the tool or language object.",
    )
    icon_url = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="URL",
        help_text="Copy paste the url which leads to the tool's or language's icon.",
    )
    icon_file = models.FileField(
        null=True,
        blank=True,
        upload_to="home/tool_or_language_icons",
        help_text=(
            "<strong>Note: </strong><li>Accepted file type is svg.</li>"
            "<li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['svg']), validate_file_size],
    )
    alt = models.TextField(
        max_length=500,
        null=False,
        blank=False,
        default="lorem ipsum",
        verbose_name="Alternative Text",
        help_text=(
            "The alt attribute provides alternative information for an image "
            "if a user for some reason cannot view it (because of slow connection, "
            "an error in the src attribute, or if the user uses a screen reader)."
        ),
    )
    
    class Meta:
        
        verbose_name_plural = "Home Page Tools & Languages"
    
    def __str__(self):
        
        return self.title

class HomePageInterest(TranslatableModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name="Universal Unique Identifier",
        help_text="Universal Unique Identifier",
    )

    translation = TranslatedFields(
        title = models.CharField(
            max_length=255,
            null=False,
            blank=False,
            default="Lorem Ipsum",
        ),
        description = models.TextField(
            max_length=10000,
            null=True,
            blank=True,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )    

    class Meta:

        verbose_name_plural = "Home Page Interests"
    
    def __str__(self):
        
        return self.title

class HomePagePartnersSectionTextContent(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(
            max_length=300,
            null=False,
            blank=False,
            default="Lorem Ipsum",
            help_text="Write a header for partners section.",
        ),
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text="Write a paragraph or sentence for partners section.",
        ),
    )

    class Meta:

        verbose_name_plural = "Home Page Partners Section Text Contents"

class HomePagePartner(TranslatableModel):

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        default="Lorem Ipsum",
        help_text="Write your partner's company's name.",
    )
    logo = models.ImageField(
        verbose_name="Image",
        null=False,
        blank=False,
        default="assets/default.jpg",
        upload_to="home/partner_logos",
        help_text=(
            "<strong>Notes: </strong><li>Resize the logo to 200px x 200px.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change "
            "file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )

    translations = TranslatedFields(
        logo_alt = models.TextField(
            verbose_name="Alternative Text for The Partner's Logo",
            max_length=1000,
            null=False,
            blank=False,
            default="Lorem Ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if "
                "a user for some reason cannot view it (because of slow connection, an error in "
                "the src attribute, or if the user uses a screen reader)."
            ),
        ),
    )

    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="URL",)

    class Meta:

        verbose_name_plural = "Home Page Partners"

    def __str__(self):

        return f'{self.name}'



##############################

# CONTACT PAGE

##############################

class ContactPageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Contact Page Meta Descriptions"

class ContactPageHeroSection(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(max_length=250, blank=False, null=False, default="Lorem Ipsum"),
        image = models.ImageField(
            null=False,
            blank=False,
            default="assets/default.jpg",
            upload_to='home/hero_section',
            help_text=(
                "<strong>Note: </strong><li>Dimension requirement is 1.3 height/width</li>"
                "<li>Don't forget to scale down your images to increase load speed.</li>"
                "<li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change the file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        text = models.TextField(
            max_length=10000,
            blank=False,
            null=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", 
            help_text=(
                "<strong>Notes: </strong><li>Introduce your self.</li>"
                "<li>Include the most relevant professional experience.</li>"
                "<li>Mention significant personal achievements or awards.</li>"
                "<li>Introduce personal details.</li><li>Use a casual and friendly tone.</li>"
            ),
        ),
        alt = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as '
                'it relates to the content of a document or webpage. It is read aloud '
                'to users by screen reader software, and it is indexed by search engines. '
                'It\'s good for better search engine optimization.'
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Contact Page Hero Sections"

class ContactPageMainVisual(TranslatableModel):

    translations = TranslatedFields(
        image = models.ImageField(
            null=True,
            blank=True,
            upload_to='contact',
            help_text=(
                "Share an image that will encourage the visitors/gamers to tell their problem."
                "<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change file type/extension</li>"
                "<li>This application prefers image over video by default. And, only one of "
                "them will be displayed</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        video = models.FileField(
            null=True,
            blank=True,
            upload_to="contact",
            help_text=(
                "Upload image or video. This application can't display both. "
                "(Image is preferred.)<br><br><strong>Note: </strong>"
                "<li>Accepted file types are mp4, mov and, avi</li>"
                "<li>You can use ShotCut to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['mp4', 'mov', 'avi']), validate_file_size],
        ),
        alt = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as '
                'it relates to the content of a document or webpage. It is read aloud '
                'to users by screen reader software, and it is indexed by search engines. '
                'It\'s good for better search engine optimization.'
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Contact Page Main Visuals"

class ContactPageMessage(models.Model):

    full_name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        default="N/A",
        verbose_name="Full Name",
    )
    sender_email = models.EmailField(
        max_length=300,
        null=False,
        blank=False,
        default="N/A",
        verbose_name="Email",
    )
    phone_num = PhoneNumberField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    message = models.TextField(max_length=10000, null=False, blank=False, default="N/A", verbose_name="Message",)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User",)
    ip_address = models.GenericIPAddressField(null=False, blank=False, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="User Agent",
        default="N/A",
    )
    sending_time = models.DateTimeField(blank=False, null=False, verbose_name="Send Time", default=timezone.now,)

    def send_emails(self):

        subject = "New Contact Message"
        message = "New Contact Message"
        from_email = f'Doga Ege Ozden\'s Site<{EMAIL_HOST_USER}>'
        to_email = ['dogaegeozden@gmail.com',]
        html_message = render_to_string('contact/contact_message_email.html', {'contact_message': self, 'message': message,})

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
            html_message=html_message,
        )

    class Meta:

        verbose_name_plural = "Contact Page Messages"