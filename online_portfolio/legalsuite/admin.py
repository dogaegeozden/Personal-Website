# MODULES AND LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODELS
from .models import (
    PrivacyPolicyAgreementsPageMetaDescription,
    PrivacyPolicyAgreement,
    PrivacyPolicyAgreementSection,

    TermsAndConditionsAgreementsPageMetaDescription,
    TermsAndConditionsAgreement,
    TermsAndConditionsAgreementSection,
)



# REGISTRATIONS

##############################

# PRIVACY POLICY PAGE

##############################

@admin.register(PrivacyPolicyAgreementsPageMetaDescription)
class PrivacyPolicyAgreementsPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(PrivacyPolicyAgreement)
class PrivacyPolicyAgreementAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'create_time',)

    fieldsets = (
        ('Privacy Policy Agreement', {
            'fields': (
                'id',
                'title',
                'meta_description',
                'effective_date',
                'create_time',
            )
        }),
    )

@admin.register(PrivacyPolicyAgreementSection)
class PrivacyPolicyAgreementSectionAdmin(TranslatableAdmin):

    fieldsets = (
        ('Privacy Policy Agreement Section', {
            'fields': (
                'agreement',
                'title',
                'text',
                'list_item_1',
                'list_item_2',
                'list_item_3',
                'list_item_4',
                'list_item_5',
                'list_item_6',
                'list_item_7',
                'list_item_8',
                'list_item_9',
                'list_item_10',
            )
        }),
    )


##############################

# TERMS AND CONDITIONS PAGE

##############################

@admin.register(TermsAndConditionsAgreementsPageMetaDescription)
class TermsAndConditionsAgreementsPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(TermsAndConditionsAgreement)
class TermsAndConditionsAgreementAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'create_time',)

    fieldsets = (
        ('Terms And Conditions Agreement', {
            'fields': (
                'id',
                'title',
                'meta_description',
                'effective_date',
                'create_time',
            )
        }),
    )

@admin.register(TermsAndConditionsAgreementSection)
class TermsAndConditionsAgreementSectionAdmin(TranslatableAdmin):

    fieldsets = (
        ('Terms And Conditions Agreement Section', {
            'fields': (
                'agreement',
                'title',
                'text',
                'list_item_1',
                'list_item_2',
                'list_item_3',
                'list_item_4',
                'list_item_5',
                'list_item_6',
                'list_item_7',
                'list_item_8',
                'list_item_9',
                'list_item_10',
            )
        }),
    )