# MODULES AND LIBRARIES
from django.db import models
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import get_language



# DATA CLASSES

##############################

# PRIVACY POLICY PAGE

##############################

class PrivacyPolicyAgreementsPageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                "ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit "
                "in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
                "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            ),
        ),
    )

    class Meta:
        
        verbose_name_plural = "Privacy Policy Agreements Page Meta Descriptions"
        db_table = "legalsuite_ppagreementspagemetadescription"
        
class PrivacyPolicyAgreement(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Title", default="Lorem Ipsum",)
    meta_description = models.TextField(
        max_length=1500,
        null=False,
        blank=False,
        default=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
            "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
            "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
            "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        ),
        help_text="Ensure this description is engaging and includes primary keywords.",
    )
    effective_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Effective Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )
    create_time = models.DateTimeField(blank=False, null=False, verbose_name="Create Time", default=timezone.now,)

    def __str__(self):

        return f'{self.title} - {self.id}'

    def get_absolute_url(self):
    
        lang = get_language()
    
        if lang == "tr":
    
            return reverse("privacy-policy-agreement-detail-translated", kwargs={"id": self.pk})
    
        return reverse("privacy-policy-agreement-detail", kwargs={"id": self.pk})

    class Meta:
        
        verbose_name_plural = 'Privacy Policy Agreements'

class PrivacyPolicyAgreementSection(TranslatableModel):

    agreement = models.ForeignKey(
        'PrivacyPolicyAgreement',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Agreement",
    )

    translations = TranslatedFields(
        title = models.CharField(
            max_length=500,
            null=True,
            blank=True,
            help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.",
        ),
        text = models.TextField(
            max_length=10000,
            null=True,
            blank=True,
            help_text="Write section's content, and make sure you are using a proper language.",
        ),
        list_item_1 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_2 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_3 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_4 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_5 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_6 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_7 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_8 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_9 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_10 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
    )

    class Meta:

        verbose_name_plural = "Privacy Policy Agreement Sections"



##############################

# TERMS AND CONDITIONS PAGE

##############################

class TermsAndConditionsAgreementsPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
                "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis "
                "aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
                "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui "
                "officia deserunt mollit anim id est laborum."
            ),
        ),
    )

    class Meta:
    
        verbose_name_plural = "Terms And Conditions Agreements Page Meta Descriptions"
        db_table = "legalsuite_tcagreementspagemetadescription"

class TermsAndConditionsAgreement(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Title", default="Lorem Ipsum",)
    meta_description = models.TextField(
        max_length=1500,
        null=False,
        blank=False,
        default=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
            "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
            "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
            "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        ),
        help_text="Ensure this description is engaging and includes primary keywords.",
    )
    effective_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Effective Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )
    create_time = models.DateTimeField(blank=False, null=False, verbose_name="Create Time", default=timezone.now,)

    def __str__(self):

        return f'{self.title} - {self.id}'

    def get_absolute_url(self):
    
        lang = get_language()
    
        if lang == "tr":
    
            return reverse("terms-and-conditions-agreement-detail-translated", kwargs={"id": self.pk})
    
        return reverse("terms-and-conditions-agreement-detail", kwargs={"id": self.pk})

    class Meta:

        verbose_name_plural = 'Terms And Conditions Agreements'

class TermsAndConditionsAgreementSection(TranslatableModel):

    agreement = models.ForeignKey(
        'TermsAndConditionsAgreement',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Agreement",
    )

    translations = TranslatedFields(
        title = models.CharField(
            max_length=500,
            null=True,
            blank=True,
            help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.",
        ),
        text = models.TextField(
            max_length=10000,
            null=True,
            blank=True,
            help_text="Write section's content, and make sure you are using a proper language.",
        ),
        list_item_1 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_2 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_3 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_4 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_5 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_6 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_7 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_8 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_9 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
        list_item_10 = models.TextField(
            max_length=4000,
            null=True,
            blank=True,
        ),
    )

    class Meta:

        verbose_name_plural = "Terms And Conditions Agreement Sections"