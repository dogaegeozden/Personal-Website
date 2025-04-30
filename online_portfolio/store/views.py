# MODULES AND LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

# MODELS
from .models import (
    GamesPageMetaDescription,
    GamesPageGame,

    OpenSourcePageMetaDescription,
    OpenSourcePageApplication,

    ServicesPageService,
    ServicesPageMetaDescription,
    ServicesPageMainContent,
    ServiceDetailPageServiceInclusion,
    ServiceDetailPageProcessStep,
    ServiceDetailPageServiceInquiry,

    ApplicationsPageMetaDescription,
    ApplicationsPageApplication,
)
from accountportal.models import Profile
from brandmanager.models import (
    GlobalBrandIdentity,
    GlobalContactInformation,
)

# FORMS
from .forms import ServiceInquiryForm

# ONLINE PORTFOLIO FUNCTIONS
from modules.visitor_inspector import (
    get_user,
    get_ip,
    get_user_agent,
)
from modules.data_processing import (
    process_app_download_data,
)
from modules.logging_config import (
    debug,
    info,
    warning,
    error,
)



# VIEW FUNCTIONS

##############################

# GAMES PAGE

##############################

def games(request):

    all_games_objs = GamesPageGame.objects.all()
    all_meta_description_objs = GamesPageMetaDescription.objects.all()

    context = {
        'all_games_objs': all_games_objs,
        'all_meta_description_objs': all_meta_description_objs,
    }

    return render(request, 'games/games.html', context=context)

def game_detail(request, slug):

    game_content = get_object_or_404(GamesPageGame, slug=slug)
    
    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    process_app_download_data(request=request, user=user, ip=ip, user_agent=user_agent)

    context = {
        'game_content': game_content,
    }

    return render(request, 'games/game_detail.html', context=context)



##############################

# OPEN SOURCE PAGE

##############################

def open_source_apps(request):

    all_open_source_app_objs = OpenSourcePageApplication.objects.all()
    all_meta_description_objs = OpenSourcePageMetaDescription.objects.all()

    context = {
        'all_open_source_app_objs': all_open_source_app_objs,
        'all_meta_description_objs': all_meta_description_objs,
    }

    return render(request, 'open_source_apps/open_source_apps.html', context=context)

def open_source_app_detail(request, slug):

    open_source_app = get_object_or_404(OpenSourcePageApplication, slug=slug)
    
    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    process_app_download_data(request=request, user=user, ip=ip, user_agent=user_agent)

    context = {
        'open_source_app': open_source_app,
    }

    return render(request, 'open_source_apps/open_source_app_detail.html', context=context)



##############################

# SERVICES PAGE

##############################

def services(request):

    all_meta_description_objs = ServicesPageMetaDescription.objects.all()
    all_services_page_main_content_objs = ServicesPageMainContent.objects.all()
    all_service_objs = ServicesPageService.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_services_page_main_content_objs': all_services_page_main_content_objs,
        'all_service_objs': all_service_objs,
    }

    return render(request, 'services/services.html', context=context)

def service_detail(request, slug):

    service = get_object_or_404(ServicesPageService, translations__slug=slug)

    is_service_detail_page_success_message_exists = False
    is_service_detail_page_error_message_exists = False

    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    all_service_inclusion_objs = ServiceDetailPageServiceInclusion.objects.filter(service=service)
    all_service_process_step_objs = ServiceDetailPageProcessStep.objects.filter(service=service)

    service_inquiry_form = ServiceInquiryForm()
    
    if request.method == "POST" and "submitServiceInquiryBtn" in request.POST:

        service_inquiry_form = ServiceInquiryForm(request.POST)

        if service_inquiry_form.is_valid():

            try:

                ServiceDetailPageServiceInquiry.objects.create(
                    service_choice=service.title,
                    name=service_inquiry_form.cleaned_data['name'],
                    email=service_inquiry_form.cleaned_data['email'],
                    phone_number=service_inquiry_form.cleaned_data['phone_number'],
                    project_details=service_inquiry_form.cleaned_data['project_details'],
                    ip_address=ip,
                    user_agent=user_agent,
                    user=user,
                )
                service_inquiry_form = ServiceInquiryForm()
                is_service_detail_page_success_message_exists = True
                info("Service inquiry has been delivered!")
                messages.success(request, "Your service inquiry has been delivered!")

            except Exception as e:

                is_service_detail_page_error_message_exists = True
                error(f"Error during inquiring a service: {e}")
                messages.error(
                    request,
                    f"Error during inquiring a service: {e}",
                )

        else:

            is_service_detail_page_error_message_exists = True
            warning(service_inquiry_form.errors)
            messages.error(request, service_inquiry_form.errors)

    context = {
        'service': service,
        'all_service_inclusion_objs': all_service_inclusion_objs,
        'all_service_process_step_objs': all_service_process_step_objs,
        'service_inquiry_form': service_inquiry_form,
        'is_service_detail_page_success_message_exists': is_service_detail_page_success_message_exists,
        'is_service_detail_page_error_message_exists': is_service_detail_page_error_message_exists,
    }

    return render(request, 'services/service_detail.html', context=context)



##############################

# APPLICATIONS PAGE

##############################

def applications(request):

    all_meta_description_objs = ApplicationsPageMetaDescription.objects.all()
    all_application_objs = ApplicationsPageApplication.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_application_objs': all_application_objs,
    }

    return render(request, 'applications/applications.html', context=context)

def application_detail(request, slug):

    application = get_object_or_404(ApplicationsPageApplication, slug=slug)

    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    process_app_download_data(request=request, user=user, ip=ip, user_agent=user_agent)

    context = {
        'application': application,
    }

    return render(request, 'applications/application_detail.html', context=context)
