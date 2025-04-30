# MODULES AND LIBRARIES
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import FileExtensionValidator

# ONLINE PORTFOLIO MODULES
from modules.validators import validate_file_size



# DATA CLASSES

##############################

# GLOBAL MODELS

##############################

class GlobalBrandIdentity(TranslatableModel):

    icon = models.FileField(
        null=False,
        blank=False,
        verbose_name="Brand Icon",
        default="assets/default.ico",
        upload_to='brand_identity',
        help_text=(
            "<strong>Note: </strong><li>It needs to be .ico file</li>"
            "<li>You can use GIMP to convert png/jpg/jpeg and the like files to .ico files</li>"
            "<li>Make sure the file size is below 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['ico']), validate_file_size],
    )
    logo = models.ImageField(
        null=False,
        blank=False,
        verbose_name="Brand Logo",
        default="assets/default.jpg",
        upload_to="brand_identity",
        help_text=(
            "<strong>Note:</strong><li>Don't forget to scale down your image to "
            "improve web page performance.</li><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
            "<li>You can use GIMP to convert file types</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    header_logo = models.ImageField(
        null=False,
        blank=False,
        verbose_name="Header Logo",
        default="assets/default.jpg",
        upload_to="brand_identity",
        help_text=(
            "<strong>Note:</strong><li>Don't forget to scale down your image to "
            "improve web page performance.</li><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
            "<li>You can use GIMP to convert file types</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    brand_name = models.CharField(
        null=False,
        blank=False,
        verbose_name="Brand Name",
        max_length=200,
        default="Lorem Ipsum",
    )
    official_company_name = models.CharField(
        null=False,
        blank=False,
        verbose_name="Official Company Name",
        max_length=250,
        default="Lorem Ipsum",
    )
    translations = TranslatedFields(
        copy_right_text = models.TextField(
            verbose_name="Copy Right Text",
            max_length=1500,
            null=False,
            blank=False,
            default="Copyright © 2024 Lorem Ipsum. All Rights Reserved.",
        ),
        slogan = models.CharField(null=False, blank=False, verbose_name="Slogan", max_length=200, default="Lorem Ipsum",),
        logo_alt = models.TextField(
            null=False,
            blank=False,
            verbose_name="Alternative Text for The Logo",
            max_length=500,
            default="Lorem Ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image "
                "if a user for some reason cannot view it (because of slow connection, an "
                "error in the src attribute, or if the user uses a screen reader)."
            ),
        ),
        header_logo_alt = models.TextField(
            null=False,
            blank=False,
            verbose_name="Alternative Text for The Header Logo",
            max_length=500,
            default="Lorem Ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image "
                "if a user for some reason cannot view it (because of slow connection, an "
                "error in the src attribute, or if the user uses a screen reader)."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Global Brand Identities"

class GlobalContactInformation(models.Model):

    info_email = models.CharField(max_length=300, null=True, blank=True, verbose_name="Info Email",)
    service_inquiry_email = models.CharField(max_length=300, null=True, blank=True, verbose_name="Service Inquiry Email",)
    customer_support_email = models.CharField(max_length=300, null=True, blank=True, verbose_name="Customer Support Email",)
    phone_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Phone Number",)
    office_address = models.CharField(max_length=500, null=True, blank=True, verbose_name="Office Address",)
    invoice_address = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Invoice Address",)
    website = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Website",)
    tax_number = models.CharField(max_length=300, null=True, blank=True, verbose_name="Tax Number",)

    class Meta:

        verbose_name_plural = "Global Contact Informations"

class GlobalSocialMediaLinks(models.Model):

    youtube = models.URLField(verbose_name="YouTube", max_length=1000, null=True, blank=True,)
    facebook = models.URLField(verbose_name="Facebook", max_length=1000, null=True, blank=True,)
    x = models.URLField(verbose_name="X", max_length=1000, null=True, blank=True,)
    instagram = models.URLField(verbose_name="Instagram", max_length=1000, null=True, blank=True,)
    github = models.URLField(verbose_name="GitHub", max_length=1000, null=True, blank=True,)
    linkedin = models.URLField(verbose_name="LinkedIn", max_length=1000, null=True, blank=True,)
    tiktok = models.URLField(verbose_name="TikTok", max_length=1000, null=True, blank=True,)
    
    class Meta:

        verbose_name_plural = "Global Social Media Links"