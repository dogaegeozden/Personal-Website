# MODULES AND LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODELS
from .models import (
    GamesPageMetaDescription,
    GamesPageGame,

    OpenSourcePageMetaDescription,
    OpenSourcePageApplication,

    ServicesPageMetaDescription,
    ServicesPageMainContent,
    ServicesPageService,
    ServiceDetailPageServiceInclusion,
    ServiceDetailPageProcessStep,
    ServiceDetailPageServiceInquiry,

    ApplicationsPageMetaDescription,
    ApplicationsPageApplication,
)



# REGISTRATIONS

##############################

# GAMES PAGE

##############################

@admin.register(GamesPageMetaDescription)
class GamesPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(GamesPageGame)
class GamesPageGameAdmin(TranslatableAdmin):

    readonly_fields=('id', 'posting_time',)

    fieldsets = (
        ('Game Content', {
            'fields': (
                'id',
                'slug',
                'title',
                'thumbnail_picture',
                'supported_devices',
                'coming_soon_status',
                'title_preview',
                'main_image_portrait',
                'main_image_landscape',
                'header1',
                'image1',
                'text1',
                'header2',
                'image2',
                'text2',
                'header3',
                'image3',
                'text3',
                'header4',
                'image4',
                'text4',
                'header5',
                'image5',
                'text5',
                'video1',
                'video2',
                'video3',
                'video4',
                'video5',
                'youtube_url1',
                'youtube_url2',
                'youtube_url3',
                'youtube_url4',
                'youtube_url5',
                'posting_time',
            )
        }),

        ('Download Links', {
            'fields': (
                'google_play_download_link',
                'apple_store_download_link',
                'microsoft_store_download_link',
            )
        }),

        ('SEO (Search Engine Optimization)', {
            'fields': (
                'meta_description',
                'main_visual_alt',
                'image_alt1',
                'image_alt2',
                'image_alt3',
                'image_alt4',
                'image_alt5',
                'video_alt1',
                'video_alt2',
                'video_alt3',
                'video_alt4',
                'video_alt5',
            )
        }),
    )



##############################

# OPEN SOURCE APPS PAGE

##############################

@admin.register(OpenSourcePageMetaDescription)
class OpenSourcePageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(OpenSourcePageApplication)
class OpenSourcePageApplicationAdmin(TranslatableAdmin):

    readonly_fields=('id', 'posting_time',)

    fieldsets = (
        ('Open Source Application Information & Content', {
            'fields': (
                'id',
                'slug',
                'posting_time',
                'title',
                'supported_devices',
                'introduction_paragraph',
                'thumbnail_picture',
                'github_link',
                'header1',
                'image1',
                'text1',
                'header2',
                'image2',
                'text2',
                'header3',
                'image3',
                'text3',
            )
        }),

        ('SEO (Search Engine Optimization)', {
            'fields': ('meta_description', 'thumbnail_picture_alt', 'image_alt1', 'image_alt2', 'image_alt3',)
        }),
    )



##############################

# SERVICES PAGE

##############################

@admin.register(ServicesPageMetaDescription)
class ServicesPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(ServicesPageMainContent)
class ServicesPageMainContentAdmin(TranslatableAdmin):

    fieldsets = (
        ('Services Page Main Content', {
            'fields': (
                'video',
                'image',
                'alt',
                'title',
                'para1',
                'para2',
                'para3',
                'list_item1',
                'list_item2',
                'list_item3',
                'list_item4',
                'list_item5',
                'list_item6',
            )
        }),
    )

@admin.register(ServicesPageService)
class ServicesPageServiceAdmin(TranslatableAdmin):

    readonly_fields=('id', 'posting_time',)

    fieldsets = (
        ('Service Information & Content', {
            'fields': (
                'id',
                'posting_time',
                'slug',
                'title',
                'thumbnail_picture',
                'call_to_action_sentence',
                'short_summary',
            )
        }),
        ('SEO (Search Engine Optimization)', {
            'fields': (
                'meta_description',
                'thumbnail_pic_alt',
            )
        }),
    )

@admin.register(ServiceDetailPageServiceInclusion)
class ServiceDetailPageServiceInclusionAdmin(TranslatableAdmin):

    readonly_fields=('id', 'create_time',)
    list_display = ('service', 'title', 'id',)
    list_filter = ('service',)

    fieldsets = (
        ('Service Inclusion', {
            'fields': (
                'id',
                'service',
                'title',
                'text',
                'create_time',
            )
        }),
    )

@admin.register(ServiceDetailPageProcessStep)
class ServiceDetailPageProcessStepAdmin(TranslatableAdmin):

    readonly_fields=('id', 'create_time',)
    list_display = ('service', 'title', 'step_number',)
    list_filter = ('service', 'step_number',)

    fieldsets = (
        ('Process Step', {
            'fields': (
                'id',
                'service',
                'step_number',
                'title',
                'image',
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
                'create_time',
            )
        }),
        ('SEO (Search Engine Optimization)', {
            'fields': (
                'alt',
            )
        }),
    )

@admin.register(ServiceDetailPageServiceInquiry)
class ServiceDetailPageServiceInquiryAdmin(admin.ModelAdmin):

    readonly_fields = (
        'service_choice',
        'name',
        'email',
        'phone_number',
        'project_details',
        'user',
        'ip_address',
        'user_agent',
        'submit_time',
    )

    fieldsets = (
        ('Service Information & Content', {
            'fields': (
                'service_choice',
                'name',
                'email',
                'phone_number',
                'project_details',
                'user',
                'ip_address',
                'user_agent',
                'submit_time',
            )
        }),
    )



##############################

# APPLICATIONS PAGE

##############################

@admin.register(ApplicationsPageMetaDescription)
class ApplicationsPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(ApplicationsPageApplication)
class ApplicationsPageApplicationAdmin(TranslatableAdmin):

    readonly_fields=('id', 'posting_time',)

    fieldsets = (
        ('Application Content', {
            'fields': (
                'id',
                'slug',
                'title',
                'thumbnail_picture',
                'supported_devices',
                'main_visual_portrait',
                'main_visual_landscape',
                'introduction_paragraph',
                'price',
                'header1',
                'image1',
                'text1',
                'header2',
                'image2',
                'text2',
                'header3',
                'image3',
                'text3',
                'posting_time',
            )
        }),

        ('Download Links', {
            'fields': (
                'google_play_download_link',
                'apple_store_download_link',
                'microsoft_store_download_link',
            )
        }),

        ('SEO (Search Engine Optimization)', {
            'fields': (
                'meta_description',
                'thumbnail_picture_alt',
                'main_visual_alt',
                'image_alt1',
                'image_alt2',
                'image_alt3',
            )
        }),
    )