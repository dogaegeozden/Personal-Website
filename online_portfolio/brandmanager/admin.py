# MODULES AND LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODELS
from .models import (
    GlobalBrandIdentity,
    GlobalSocialMediaLinks,
    GlobalContactInformation,
)



# REGISTRATIONS

##############################

# GLOBAL REGISTRATIONS

##############################

@admin.register(GlobalBrandIdentity)
class GlobalBrandIdentityAdmin(TranslatableAdmin):

    fieldsets = (
        ('Portfolio Icon', {
            'fields': (
                'icon',
                'logo',
                'header_logo',
                'brand_name',
                'official_company_name',
                'copy_right_text',
                'slogan',
                'logo_alt',
                'header_logo_alt',
            )
        }),
    )

@admin.register(GlobalSocialMediaLinks)
class GlobalSocialMediaLinksAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Social Media Links', {
            'fields': ('linkedin', 'instagram', 'facebook', 'youtube', 'github', 'x', 'tiktok',)
        }),
    )

@admin.register(GlobalContactInformation)
class GlobalContactInformationAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Contact Information', {
            'fields': (
                'info_email',
                'service_inquiry_email',
                'customer_support_email',
                'phone_number',
                'office_address',
                'invoice_address',
                'website',
                'tax_number',
            )
        }),
    )