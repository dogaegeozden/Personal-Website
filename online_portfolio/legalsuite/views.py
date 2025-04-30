# MODULES AND LIBRARIES
from django.shortcuts import render, get_object_or_404

# MODELS
from .models import (
    PrivacyPolicyAgreementsPageMetaDescription,
    PrivacyPolicyAgreement,
    PrivacyPolicyAgreementSection,

    TermsAndConditionsAgreementsPageMetaDescription,
    TermsAndConditionsAgreement,
    TermsAndConditionsAgreementSection,
)



# VIEW FUNCTIONS

##############################

# PRIVACY POLICY AGREEMENTS PAGE

##############################

def privacy_policy_agreements(request):

    all_meta_description_objs = PrivacyPolicyAgreementsPageMetaDescription.objects.all()
    all_privacy_policy_agreement_objs = PrivacyPolicyAgreement.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_privacy_policy_agreement_objs': all_privacy_policy_agreement_objs,
    }

    return render(request, 'privacy_policy/privacy_policy_agreements.html', context=context)

def privacy_policy_agreement_detail(request, id):

    privacy_policy_detail = get_object_or_404(PrivacyPolicyAgreement, id=id)
    all_privacy_policy_section_objs = PrivacyPolicyAgreementSection.objects.filter(agreement=privacy_policy_detail)

    context = {
        'privacy_policy_detail': privacy_policy_detail,
        'all_privacy_policy_section_objs': all_privacy_policy_section_objs,
    }

    return render(request, 'privacy_policy/privacy_policy_agreement_detail.html', context=context)



##############################

# TERMS AND CONDITIONS AGREEMENTS PAGE

##############################

def terms_and_conditions_agreements(request):

    all_meta_description_objs = TermsAndConditionsAgreementsPageMetaDescription.objects.all()
    all_terms_and_conditions_agreement_objs = TermsAndConditionsAgreement.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_terms_and_conditions_agreement_objs': all_terms_and_conditions_agreement_objs,
    }

    return render(request, 'terms_and_conditions/terms_and_condition_agreements.html', context)

def terms_and_conditions_agreement_detail(request, id):

    terms_and_conditions_detail = get_object_or_404(TermsAndConditionsAgreement, id=id)
    all_terms_and_conditions_agreement_section_objs = TermsAndConditionsAgreementSection.objects.filter(
        agreement=terms_and_conditions_detail,
    )

    context = {
        'terms_and_conditions_detail': terms_and_conditions_detail,
        'all_terms_and_conditions_agreement_section_objs': all_terms_and_conditions_agreement_section_objs,
    }

    return render(request, 'terms_and_conditions/terms_and_conditions_agreement_detail.html', context)