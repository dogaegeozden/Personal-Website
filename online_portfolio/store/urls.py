# MODULES & LIBRARIES
from django.urls import path
from django.utils.translation import gettext_lazy

# VIEW FUNCTIONS
from .views import (
    games,
    game_detail,

    open_source_apps,
    open_source_app_detail,

    services,
    service_detail,

    applications,
    application_detail,
)

# URL PATTERS
urlpatterns = [
    path(gettext_lazy('open_source_apps/'), open_source_apps, name="open-source-apps"),
    path("open_source_apps/<slug:slug>/", open_source_app_detail, name="open-source-app-detail"),
    path("acik_kaynak_uygulamalar/<slug:slug>/", open_source_app_detail, name="open-source-app-detail-translated"),
    path(gettext_lazy('games/'), games, name='games'),
    path("games/<slug:slug>/", game_detail, name="game-detail"),
    path("oyunlar/<slug:slug>/", game_detail, name="game-detail-translated"),
    path(gettext_lazy('services/'), services, name='services'),
    path("services/<slug:slug>/", service_detail, name="service-detail"),
    path("hizmetler/<slug:slug>/", service_detail, name="service-detail-translated"),
    path(gettext_lazy('applications/'), applications, name='applications'),
    path("applications/<slug:slug>/", application_detail, name="application-detail"),
    path("uygulamalar/<slug:slug>/", application_detail, name="application-detail-translated"),
]