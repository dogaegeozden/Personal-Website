# MODULES AND LIBRARIES
from django.urls import path
from django.utils.translation import gettext_lazy

# VIEW FUNCTIONS
from .views import (
    privacy_policy_agreements,
    privacy_policy_agreement_detail,
    terms_and_conditions_agreements,
    terms_and_conditions_agreement_detail,
)

# URL PATTERNS
urlpatterns = [
    path(gettext_lazy('privacy_policy_agreements/'), privacy_policy_agreements, name="privacy-policy-agreements"),
    path('privacy_policy_detail/<uuid:id>', privacy_policy_agreement_detail, name="privacy-policy-agreement-detail"),
    path('gizlilik_politikasi_detayi/<uuid:id>', privacy_policy_agreement_detail, name="privacy-policy-agreement-detail-translated"),
    path(gettext_lazy('terms_and_conditions_agreements/'), terms_and_conditions_agreements, name="terms-and-conditions-agreements"),
    path('terms_and_conditions_detail/<uuid:id>', terms_and_conditions_agreement_detail, name="terms-and-conditions-agreement-detail"),
    path('sartlar_ve_kosullar_ayrintisi/<uuid:id>', terms_and_conditions_agreement_detail, name="terms-and-conditions-agreement-detail-translated"),
]