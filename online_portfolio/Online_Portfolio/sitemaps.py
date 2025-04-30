# MODULES AND LIBRARIES
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# MODELS
from store.models import (
    ServicesPageService,
    GamesPageGame,
    OpenSourcePageApplication,
    ApplicationsPageApplication,
)
from legalsuite.models import (
    PrivacyPolicyAgreement,
    TermsAndConditionsAgreement,
)



##############################

# STATIC

##############################

class StaticViewSitemap(Sitemap):

    priority = 0.5
    changefreq = 'yearly'

    def items(self):

        return [
            'home',
            'services',
            'games',
            'applications',
            'open-source-apps',
            'success-stories',
            'projects',
            'blog',
            'contact',
            'login',
            'register',
            'privacy-policy-agreements',
            'terms-and-conditions-agreements',
        ]

    def location(self, item):

        return reverse(item)



##############################

# SERVICES

##############################

class ServicesViewSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):

        return ServicesPageService.objects.all()

    def lastmod(self, obj):

        return obj.posting_time

    def location(self, obj):

        return obj.get_absolute_url()



##############################

# GAMES

##############################

class GamesViewSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):

        return GamesPageGame.objects.all()

    def lastmod(self, obj):

        return obj.posting_time

    def location(self, obj):

        return obj.get_absolute_url()



##############################

# OPEN SOURCE APPS

##############################

class OpenSourcePageApplicationViewSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):

        return OpenSourcePageApplication.objects.all()

    def lastmod(self, obj):

        return obj.posting_time

    def location(self, obj):

        return obj.get_absolute_url()



##############################

# APPLICATIONS

##############################

class ApplicationsPageApplicationViewSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):

        return ApplicationsPageApplication.objects.all()

    def lastmod(self, obj):

        return obj.posting_time

    def location(self, obj):

        return obj.get_absolute_url()



##############################

# PRIVACY POLICY AGREEMENTS

##############################

class PrivacyPolicyAgreementsViewSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):

        return PrivacyPolicyAgreement.objects.all()

    def lastmod(self, obj):

        return obj.create_time

    def location(self, obj):

        return obj.get_absolute_url()



##############################

# TERMS AND CONDITION AGREEMENTS

##############################

class TermsAndConditionsAgreementsViewSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):

        return TermsAndConditionsAgreement.objects.all()

    def lastmod(self, obj):

        return obj.create_time

    def location(self, obj):

        return obj.get_absolute_url()