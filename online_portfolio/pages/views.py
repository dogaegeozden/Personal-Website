# LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

# FORMS
from .forms import MessageForm

# MODELS
from .models import (
    HomePageMetaDescription,
    HomePageHeroSection,
    HomePageProfilePicture,
    HomePageBio, 
    HomePageToolOrLanguage,
    HomePageInterest, 
    HomePagePartnersSectionTextContent,
    HomePagePartner,

    ContactPageMetaDescription,
    ContactPageHeroSection,
    ContactPageMainVisual,
    ContactPageMessage,
)
from datacenter.models import (
    GlobalUnsubscribeLink,
)

# ONLINE PORTFOLIO FUNCTIONS
from modules.visitor_inspector import (
    get_user,
    get_ip,
    get_user_agent,
)
from modules.logging_config import (
    info,
    error,
    warning,
)



# VIEW FUNCTIONS

##############################

# HOME PAGE

##############################

def home(request):

    all_meta_description_objs = HomePageMetaDescription.objects.all()
    all_hero_section_objs = HomePageHeroSection.objects.all()
    all_profile_picture_objs = HomePageProfilePicture.objects.all()
    all_bio_objs = HomePageBio.objects.all()
    all_tool_or_language_objs = HomePageToolOrLanguage.objects.all()
    all_interest_objs = HomePageInterest.objects.all()
    all_clients_section_text_content_objs = HomePagePartnersSectionTextContent.objects.all()
    all_partner_objs = HomePagePartner.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_hero_section_objs': all_hero_section_objs,
        'all_profile_picture_objs': all_profile_picture_objs,
        'all_bio_objs': all_bio_objs,
        'all_tool_or_language_objs': all_tool_or_language_objs,
        'all_interest_objs': all_interest_objs,
        'all_clients_section_text_content_objs': all_clients_section_text_content_objs,
        'all_partner_objs': all_partner_objs,
    }

    return render(request, 'home/home.html', context=context)



##############################

# CONTACT PAGE

##############################

def contact(request):

    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    is_contact_page_success_message_exists = False
    is_contact_page_error_message_exists = False

    all_meta_description_objs = ContactPageMetaDescription.objects.all()
    all_hero_section_objs = ContactPageHeroSection.objects.all()
    all_contact_page_main_visual_objs = ContactPageMainVisual.objects.all()
    contact_form = MessageForm()

    if request.method == "POST" and "submitBtn" in request.POST:

        contact_form = MessageForm(request.POST)

        if contact_form.is_valid():

            try:

                ContactPageMessage.objects.create(
                    full_name=contact_form.cleaned_data['full_name'],
                    sender_email=contact_form.cleaned_data['sender_email'],
                    phone_num=contact_form.cleaned_data['phone_num'],
                    message=contact_form.cleaned_data['message'],
                    user=user,
                    ip_address=ip,
                    user_agent=user_agent,
                )
                contact_form = MessageForm()
                is_contact_page_success_message_exists = True
                info("Message has been delivered!")
                messages.success(request, "Your message has been delivered!")

            except Exception as e:

                is_contact_page_error_message_exists = True
                error(f"Error during sending message: {e}")
                messages.error(request, f"An error occurred: {e}")

        else:
            
            is_contact_page_error_message_exists = True
            warning(f"Error with contact form: {contact_form.errors}")
            messages.error(request, f'{contact_form.errors}')

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_hero_section_objs': all_hero_section_objs,
        'all_contact_page_main_visual_objs': all_contact_page_main_visual_objs,
        'contact_form': contact_form,
        'is_contact_page_success_message_exists': is_contact_page_success_message_exists,
        'is_contact_page_error_message_exists': is_contact_page_error_message_exists,
    }

    return render(request, 'contact/contact.html', context=context)



##############################

# UNSUBSCRIBE PAGE

##############################

def unsubscribe(request, token):

    unsubscribe_link = get_object_or_404(GlobalUnsubscribeLink, token=token)
    subscription = unsubscribe_link.subscription

    if request.method == 'POST' and "unsubscribeBtn" in request.POST:

        try:

            subscription.delete()
            info("Subscription have been terminated!")

            return redirect('unsubscribe_success')

        except Exception as e:

            error(f"Error during unsubscription: {e}")
            messages.error(request, f"An error occurred: {e}")

    return render(request, 'unsubscribe/unsubscribe.html', {'subscription': subscription})


def unsubscribe_success(request):

    return render(request, 'unsubscribe/unsubscribe_success.html')



##############################

# 404 PAGE

##############################

def custom_404(request, exception):

    return render(request, 'custom_404/custom_404.html', status=404)