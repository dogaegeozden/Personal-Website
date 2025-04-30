# MODULES AND LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODULES
from .models import (
    SuccessStoriesPageMetaDescription,
    SuccessStoriesPageSuccessStory,

    ProjectsPageMetaDescription,
    ProjectsPageProject,
    ProjectDetailPageFeedback,

    CertificationsPageMetaDescription,
    CertificationsPageCertification,

    ResumePageMetaDescription,
    ResumePageHeroSection,
    ResumePageAboutCurrentPosition,
    ResumePageResume,
    ResumePageExperience,
    ResumePageEducation,
)



# REGISTRATIONS

##############################

# SUCCESS STORIES PAGE

##############################

@admin.register(SuccessStoriesPageMetaDescription)
class SuccessStoriesPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(SuccessStoriesPageSuccessStory)
class SuccessStoriesPageSuccessStoryAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'user', 'posting_time', 'ip_address', 'user_agent',)

    fieldsets = (
        ('Success Stories Page Success Story', {
            'fields': ('id', 'user', 'posting_time', 'job_title', 'website_link', 'text', 'ip_address', 'user_agent',)
        }),
    )



##############################

# PROJECTS PAGE

##############################

@admin.register(ProjectsPageMetaDescription)
class ProjectsPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(ProjectsPageProject)
class ProjectsPageProjectAdmin(TranslatableAdmin):

    readonly_fields = ('id', 'upload_time',)

    fieldsets = (
        ('Projects Page Project', {
            'fields': (
                'id',
                'title',
                'client',
                'project_type',
                'tags',
                'description',
                'url',
                'thumbnail_picture',
                'thumbnail_picture_alt',
                'picture1',
                'alt1',
                'picture2',
                'alt2',
                'picture3',
                'alt3',
                'picture4',
                'alt4',
                'picture5',
                'alt5',
                'picture6',
                'alt6',
                'picture7',
                'alt7',
                'picture8',
                'alt8',
                'picture9',
                'alt9',
                'upload_time',
            )
        }),
    )

@admin.register(ProjectDetailPageFeedback)
class ShowcasePageFeedbackAdmin(admin.ModelAdmin):

    readonly_fields = (
        'project_title',
        'full_name',
        'email',
        'phone_number',
        'feedback',
        'sending_time',
        'user',
        'ip_address',
        'user_agent',
    )

    fieldsets = (
        ("Feedback", {
            'fields': (
                'project_title',
                'full_name',
                'email',
                'phone_number',
                'feedback',
                'sending_time',
                'user',
                'ip_address',
                'user_agent',
            )
        }),
    )



##############################

# CERTIFICATIONS PAGE

##############################

@admin.register(CertificationsPageMetaDescription)
class CertificationsPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(CertificationsPageCertification)
class CertificationsPageCertificationAdmin(admin.ModelAdmin):

    list_display = ('title', 'topic')

    fieldsets = (
        ('Certification', {
            'fields': (
                'title',
                'topic',
                'digital_copy',
                'digital_copy_url',
                'issuer',
                'issue_date',
                'expiry_date',
            )
        }),
    )



##############################

# RESUMES PAGE

##############################

@admin.register(ResumePageResume)
class ResumePageResumeAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Resume Information & Content', {
            'fields': ('field_name', 'resume_name', 'file',)
        }),
    )

@admin.register(ResumePageHeroSection)
class ResumePageHeroSectionAdmin(TranslatableAdmin):

    fieldsets = (
        ('Hero Section Content', {
            'fields': ('title', 'image', 'alt', 'text',)
        }),
    )

@admin.register(ResumePageMetaDescription)
class ResumePageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization)', {
            'fields': ('text',)
        }),
    )

@admin.register(ResumePageAboutCurrentPosition)
class ResumePageAboutCurrentPositionAdmin(TranslatableAdmin):

    fieldsets = (
        ('Text About Your Current Position in Your Career', {
            'fields': ('text',)
        }),
    )

@admin.register(ResumePageExperience)
class ResumePageExperienceAdmin(TranslatableAdmin):

    list_display = ('job_title', 'company_name', 'start_date', 'end_date', 'working_status')

    fieldsets = (
        ('Job Information', {
            'fields': (
                'job_title',
                'company_name',
                'text',
                'header',
                'list_item_1',
                'list_item_2',
                'list_item_3',
                'list_item_4',
                'list_item_5',
                'img1',
                'alt1',
                'img2',
                'alt2',
                'img3',
                'alt3',
                'img4',
                'alt4',
                'img5',
                'alt5',
                'img6',
                'alt6',
            )
        }),

        ('Working Status', {
            'fields': ('start_date', 'end_date', 'working_status')
        }),
    )

@admin.register(ResumePageEducation)
class ResumePageEducationAdmin(TranslatableAdmin):

    fieldsets = (
        ('Education Information', {
            'fields': ('name', 'city', 'province', 'start_date', 'end_date', 'major', 'diploma', 'para', 'img',)
        }),
    )
