# MODULES & LIBRARIES
from django.contrib import admin
from parler.admin import TranslatableAdmin

# MODELS
from .models import (
    BlogPageMetaDescription,
    BlogPageBlogPost,
    BlogPagePostComment,
    BlogPagePostLike,
)



# REGISTRATIONS

##############################

# BLOG PAGE

##############################

@admin.register(BlogPageMetaDescription)
class BlogPageMetaDescriptionAdmin(TranslatableAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(BlogPageBlogPost)
class BlogPageBlogPostAdmin(admin.ModelAdmin):

    list_display = ('title', 'date',)
    list_filter = ('title', 'date',)
    readonly_fields=('id',)

    fieldsets = (
        ('Post Information & Content', {
            'fields': (
                'title',
                'id',
                'date',
                'image',
                'youtube_url',
                'video',
                'para1',
                'para2',
                'para3',
                'para4',
                'para5',
                'para6',
                'para7',
            )
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )

@admin.register(BlogPagePostComment)
class BlogPagePostCommentAdmin(admin.ModelAdmin):

    readonly_fields=('id', 'post', 'user', 'text', 'comment_time', 'ip_address', 'user_agent',)

    fieldsets = (
        ('Comments', {
            'fields': ('id', 'post', 'user', 'text', 'comment_time', 'ip_address', 'user_agent',)
        }),
    )

@admin.register(BlogPagePostLike)
class BlogPagePostLikeAdmin(admin.ModelAdmin):
    readonly_fields = ('post', 'ip_address', 'user_agent', 'like_time', 'like_status',)

    fieldsets = (
        ('Post Detail Page\'s Visitors\' Information', {
            'fields': ('post', 'ip_address', 'like_time', 'user_agent', 'like_status',)
        }),
    )