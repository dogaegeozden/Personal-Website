# MODULES AND LIBRARIES
from django.contrib import admin

# MODELS
from .models import (
    GlobalPageVisit,
    GlobalDocumentClickCoordinate,
    GlobalMouseTrace,
    GlobalKeystroke,
    GlobalSocialMediaButtonClick,
    GlobalSubscription,
    GlobalUnsubscribeLink,
    GlobalAppDownloadButtonClick,
)



# REGISTRATIONS

##############################

# GLOBAL REGISTRATIONS

##############################

@admin.register(GlobalPageVisit)
class GlobalPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('user', 'ip_address', 'user_agent', 'visit_time', 'screen_width', 'screen_height', 'page_url',)
    list_display = ('user', 'page_url', 'visit_time',)
    list_filter= ('user', 'page_url', 'visit_time',)

    fieldsets = (
        ('Page Visit', {
            'fields': ('page_url', 'user', 'ip_address', 'user_agent', 'visit_time', 'screen_width', 'screen_height',)
        }),
    )

@admin.register(GlobalDocumentClickCoordinate)
class GlobalDocumentClickCoordinateAdmin(admin.ModelAdmin):

    readonly_fields = (
        'user',
        'ip_address',
        'user_agent',
        'click_time',
        'screen_width',
        'screen_height',
        'x_coordinate',
        'y_coordinate',
        'page_url',
    )
    list_display = ('user', 'page_url', 'x_coordinate', 'y_coordinate', 'screen_width', 'screen_height', 'click_time',)
    list_filter= ('user', 'page_url', 'click_time',)

    fieldsets = (
        ('Document Click Coordinate', {
            'fields': (
                'user',
                'ip_address',
                'user_agent',
                'click_time',
                'screen_width',
                'screen_height',
                'x_coordinate',
                'y_coordinate',
                'page_url',
            )
        }),
    )

@admin.register(GlobalMouseTrace)
class GlobalMouseTraceAdmin(admin.ModelAdmin):

    readonly_fields = (
        'user',
        'ip_address',
        'user_agent',
        'movement_time',
        'screen_width',
        'screen_height',
        'x_coordinate',
        'y_coordinate',
        'page_url',
    )
    list_display = (
        'user',
        'page_url',
        'x_coordinate',
        'y_coordinate',
        'screen_width',
        'screen_height',
        'movement_time',
    )
    list_filter= ('user', 'page_url', 'movement_time',)

    fieldsets = (
        ('Mouse Trace', {
            'fields': (
                'user',
                'ip_address',
                'user_agent',
                'movement_time',
                'screen_width',
                'screen_height',
                'x_coordinate',
                'y_coordinate',
                'page_url',
            )
        }),
    )

@admin.register(GlobalSocialMediaButtonClick)
class GlobalSocialMediaButtonClickAdmin(admin.ModelAdmin):

    readonly_fields = ('user', 'ip_address', 'click_time', 'user_agent', 'platform_choice', 'page_url',)
    list_display = ('user', 'page_url', 'platform_choice', 'click_time',)
    list_filter= ('user', 'page_url', 'platform_choice', 'click_time',)


    fieldsets = (
        ('Social Media Button Click', {
            'fields': ('user', 'ip_address', 'click_time', 'user_agent', 'platform_choice', 'page_url',)
        }),
    )

@admin.register(GlobalKeystroke)
class GlobalKeystrokeAdmin(admin.ModelAdmin):

    readonly_fields = ('user', 'ip_address', 'user_agent', 'pressing_time', 'keystroke', 'page_url',)
    list_display = ('user', 'page_url', 'keystroke', 'pressing_time',)
    list_filter= ('user', 'page_url', 'pressing_time',)

    fieldsets = (
        ('Keystroke', {
            'fields': ('user', 'ip_address', 'user_agent', 'pressing_time', 'keystroke', 'page_url',)
        }),
    )

@admin.register(GlobalSubscription)
class GlobalSubscriptionAdmin(admin.ModelAdmin):

    readonly_fields=('user', 'email', 'ip_address', 'user_agent', 'subscribing_time',)
    list_display = ('user', 'email', 'subscribing_time',)
    list_filter= ('user', 'email', 'subscribing_time',)

    fieldsets = (
        ('Subscription', {
            'fields': ('user', 'email', 'ip_address', 'user_agent', 'subscribing_time',)
        }),
    )

@admin.register(GlobalUnsubscribeLink)
class GlobalUnsubscribeLinkAdmin(admin.ModelAdmin):

    readonly_fields = ('subscription', 'token',)

    fieldsets = (
        ('Brand Identity', {
            'fields': ('subscription', 'token',)
        }),
    )

@admin.register(GlobalAppDownloadButtonClick)
class GlobalAppDownloadButtonClickAdmin(admin.ModelAdmin):

    readonly_fields = ('user', 'app_choice', 'ip_address', 'user_agent', 'click_time',)

    fieldsets = (
        ('Download Button Click Information', {
            'fields': ('user', 'app_choice', 'ip_address', 'user_agent', 'click_time',)
        }),
    )