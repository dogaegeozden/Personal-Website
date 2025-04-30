# MODELS
from .models import (
    GlobalBrandIdentity,
    GlobalContactInformation,
    GlobalSocialMediaLinks,
)



# CONTEXT PROCESSORS

##############################

# BRAND IDENTITY PROCESSOR

##############################

def process_brand_identity(request):

    all_brand_identity_objs = GlobalBrandIdentity.objects.all()
    all_contact_information_objs = GlobalContactInformation.objects.all()
    all_social_media_link_objs = GlobalSocialMediaLinks.objects.all()

    context = {
        'all_brand_identity_objs': all_brand_identity_objs,
        'all_contact_information_objs': all_contact_information_objs,
        'all_social_media_link_objs': all_social_media_link_objs,
    }

    return context