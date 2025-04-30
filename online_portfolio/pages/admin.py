# LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODELS
from .models import (
    HomePageMetaDescription,
    HomePageHeroSection,
    HomePageProfilePicture,
    HomePageBio,
    HomePageToolOrLanguage,
    HomePageInterest,
    HomePagePartnersSectionTextContent,
    HomePagePartner,

    ContactPageMetaDescription,
    ContactPageMainVisual,
    ContactPageHeroSection,
    ContactPageMessage,
)



# REGISTRATIONS

##############################

# HOME PAGE

##############################

@admin.register(HomePageMetaDescription)
class HomePageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(HomePageHeroSection)
class HomePageHeroSectionAdmin(TranslatableAdmin):

    fieldsets = (
        ('Hero Section Content', {
            'fields': ('title', 'image', 'alt', 'text',)
        }),
    )

@admin.register(HomePageProfilePicture)
class HomePageProfilePictureAdmin(TranslatableAdmin):

    fieldsets = (
        ('Profile Picture', {
            'fields': ('image',)
        }),

        ('SEO (Search Engine Optimization)', {
            'fields': ('alt',)
        }),
    )

@admin.register(HomePageBio)
class HomePageBioAdmin(TranslatableAdmin):

    fieldsets = (
        ('BIO (Biography)', {
            'fields': ('name', 'text',)
        }),
    )

@admin.register(HomePageToolOrLanguage)
class HomePageToolOrLanguageAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Tool or Language', {
            'fields': ('title', 'icon_url', 'icon_file', 'alt',)
        }),
    )

@admin.register(HomePageInterest)
class HomePageInterestAdmin(TranslatableAdmin):

    readonly_fields = ('id',)

    fieldsets = (
        ('Interest Information & Content', {
            'fields': ('id', 'title', 'description',)
        }),
    )

@admin.register(HomePagePartnersSectionTextContent)
class HomePagePartnersSectionTextContentAdmin(TranslatableAdmin):

    fieldsets = (
        ('Partner Section Text Content', {
            'fields': ('title', 'text',)
        }),
    )

@admin.register(HomePagePartner)
class HomePagePartnerAdmin(TranslatableAdmin):

    fieldsets = (
        ('Client Logo', {
            'fields': ('name', 'logo', 'logo_alt', 'url',)
        }),
    )



##############################

# CONTACT PAGE

##############################

@admin.register(ContactPageMetaDescription)
class ContactPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(ContactPageHeroSection)
class ContactPageHeroSectionAdmin(TranslatableAdmin):

    fieldsets = (
        ('Hero Section Content', {
            'fields': ('title', 'image', 'alt', 'text',)
        }),
    )

@admin.register(ContactPageMainVisual)
class ContactPageMainVisualAdmin(TranslatableAdmin):

    fieldsets = (
        ('Contact Page Picture', {
            'fields': ('image',)
        }),

        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )

@admin.register(ContactPageMessage)
class ContactPageMessageAdmin(admin.ModelAdmin):

    readonly_fields = (
        'full_name',
        'sender_email',
        'phone_num',
        'message',
        'sending_time',
        'user',
        'ip_address',
        'user_agent',
    )

    fieldsets = (
        ("The Message Information", {
            'fields': (
                'full_name',
                'sender_email',
                'phone_num',
                'message',
                'sending_time',
                'user',
                'ip_address',
                'user_agent',
            )
        }),
    )