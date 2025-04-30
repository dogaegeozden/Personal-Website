# MODULES AND LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODELS
from .models import (
    LoginPageMetaDescription,

    RegisterPageMetaDescription,

    LogoutPageMetaDescription,
    
    PasswordResetCompletePageMetaDescription,
    PasswordResetConfirmPageMetaDescription,
    PasswordResetDonePageMetaDescription,
    PasswordResetFormPageMetaDescription,
    
    Profile,

    AnnouncementsPageAnnouncement,
    AnnouncementsPageUserAnnouncementView,
)



# REGISTRATIONS

##############################

# LOGIN PAGE

##############################

@admin.register(LoginPageMetaDescription)
class LoginPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )



##############################

# REGISTER PAGE

##############################

@admin.register(RegisterPageMetaDescription)
class RegisterPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )



##############################

# LOGOUT PAGE

##############################

@admin.register(LogoutPageMetaDescription)
class LogoutPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )



##############################

# PASSWORD RESET COMPLETE PAGE

##############################

@admin.register(PasswordResetCompletePageMetaDescription)
class PasswordResetCompletePageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )



##############################

# PASSWORD RESET CONFIRM PAGE

##############################

@admin.register(PasswordResetConfirmPageMetaDescription)
class PasswordResetConfirmPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )



##############################

# PASSWORD RESET DONE PAGE

##############################

@admin.register(PasswordResetDonePageMetaDescription)
class PasswordResetDonePageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )



##############################

# PASSWORD RESET FORM PAGE

##############################

@admin.register(PasswordResetFormPageMetaDescription)
class PasswordResetFormPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',) 
        }),
    )



##############################

# PROFILE PAGE

##############################

@admin.register(Profile)
class ProfilePageProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'user', 'customer_id')

    fieldsets = (
        ('User Profile', {
            'fields': (
                'id',
                'user',
                'customer_id',
                'image',
                'phone_number',
                'date_of_birth',
                'country',
                'company_name',
                'salesperson_uuid',
                'salesperson_username',
                'deliverables_password',
                'alternative_email_1',
                'alternative_email_2',
                'alternative_email_3',
                'alternative_email_4',
                'alternative_email_5',
                'alternative_email_last',
            )
        }),
    )



##############################

# ANNOUNCEMENTS PAGE

##############################

@admin.register(AnnouncementsPageAnnouncement)
class AnnouncementsPageAnnouncementAdmin(TranslatableAdmin):

    readonly_fields = ('id', 'creator', 'create_time',)

    fieldsets = (
        ('Announcements Page Announcement', {
            'fields': ('id', 'creator', 'title', 'text', 'visible_to_groups', 'create_time',)
        }),
    )

@admin.register(AnnouncementsPageUserAnnouncementView)
class AnnouncementsPageUserAnnouncementViewAdmin(admin.ModelAdmin):

    fieldset = (
        ('Announcements Page User Announcement View', {
            'fields': ('user', 'announcement', 'viewed_at',)
        })
    )