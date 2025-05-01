# MODULES AND LIBRARIES
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import set_language

# SITEMAPS
from .sitemaps import (
    StaticViewSitemap, 
    ServicesViewSitemap, 
    GamesViewSitemap,
    OpenSourcePageApplicationViewSitemap,
    ApplicationsPageApplicationViewSitemap,
    PrivacyPolicyAgreementsViewSitemap,
    TermsAndConditionsAgreementsViewSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
    'services': ServicesViewSitemap,
    'games': GamesViewSitemap,
    'opensourceapps': OpenSourcePageApplicationViewSitemap,
    'applications': ApplicationsPageApplicationViewSitemap,
    'privacypolicyagreements': PrivacyPolicyAgreementsViewSitemap,
    'termsandconditionsagreements': TermsAndConditionsAgreementsViewSitemap,
}



# URL PATTERNS

##############################

# NON-LANGUAGE SPECIFIC

##############################

urlpatterns = [
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('', include('datacenter.urls')),  # This handles the request without a language prefix
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == True:

    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

# Page Not Found (404) handler referencing to custom_404 view function.
handler404 = 'pages.views.custom_404'

if 'rosetta' in settings.INSTALLED_APPS:

    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]



##############################

# LANGUAGE SPECIFIC

##############################

urlpatterns += i18n_patterns(
    path('i18n/setlang/', set_language, name='set_language'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('pages.urls')),
    path('', include('legalsuite.urls')),
    path('', include('blog.urls')),
    path('', include('store.urls')),
    path('', include('showcase.urls')),
    path('', include('accountportal.urls')),
)