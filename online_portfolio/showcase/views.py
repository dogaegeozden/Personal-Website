# MODULES AND LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ONLINE PORTFOLIO FUNCTIONS
from modules.visitor_inspector import (
    get_user,
    get_ip,
    get_user_agent,
)
from modules.logging_config import (
    debug,
    info,
    warning,
    error,
)

# MODELS
from .models import (
    SuccessStoriesPageMetaDescription,
    SuccessStoriesPageSuccessStory,

    ProjectsPageMetaDescription,
    ProjectsPageProject,
    ProjectDetailPageFeedback,

    ResumePageMetaDescription,
    ResumePageHeroSection,
    ResumePageAboutCurrentPosition,
    ResumePageResume,
    ResumePageExperience,
    ResumePageEducation,

    CertificationsPageMetaDescription,
    CertificationsPageCertification,
)

# FORMS
from .forms import (
    SuccessStoryForm,
    FeedbackForm,
)



# VIEW FUNCTIONS

##############################

# SUCCESS STORIES PAGE

##############################

def success_stories(request):

    is_success_story_page_success_message_exists = False
    is_success_story_page_error_message_exists = False

    all_meta_description_objs = SuccessStoriesPageMetaDescription.objects.all()
    all_success_story_objs = SuccessStoriesPageSuccessStory.objects.all()

    if request.method == 'POST' and "deleteSuccessStoryBtn" in request.POST:

        try:

            SuccessStoriesPageSuccessStory.objects.get(id=request.POST.get('success_story_id')).delete()
            is_success_story_page_success_message_exists = True
            info("Success story has been deleted!")
            messages.success(request, "Your success story has been deleted!")

        except Exception as e:

            is_success_story_page_error_message_exists = True
            error(f"Error during success story deletion: {e}")
            messages.error(request, f"An error occurred: {e}") 

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_success_story_objs': all_success_story_objs,
        'is_success_story_page_success_message_exists': is_success_story_page_success_message_exists,
        'is_success_story_page_error_message_exists': is_success_story_page_error_message_exists,
    }

    return render(request, 'success_stories/success_stories.html', context=context)

@login_required
def share_your_success_story(request):

    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    is_share_your_success_story_page_success_message_exists = False
    is_share_your_success_story_page_error_message_exists = False

    success_story_form = SuccessStoryForm()

    if request.method == 'POST' and "shareBtn" in request.POST:

        success_story_form = SuccessStoryForm(request.POST)

        debug("I got the request!")

        if success_story_form.is_valid():

            debug("Form is valid.")

            try:

                SuccessStoriesPageSuccessStory.objects.create(
                    job_title=success_story_form.cleaned_data["job_title"],
                    website_link=success_story_form.cleaned_data["website_link"],
                    text=success_story_form.cleaned_data["text"],
                    user=user,
                    ip_address=ip,
                    user_agent=user_agent,
                )
                success_story_form = SuccessStoryForm()
                is_share_your_success_story_page_success_message_exists = True
                info("Success story has been shared!")
                messages.success(request, "Your success story has been shared!")

            except Exception as e:

                is_share_your_success_story_page_error_message_exists = True
                error(f"Error during success story sharing: {e}")
                messages.error(request, f"An error occurred: {e}") 

        else:
            
            is_share_your_success_story_page_error_message_exists = True
            warning(f"Error with success story form: {success_story_form.errors}")
            messages.error(request, f'{success_story_form.errors}')

    context = {
        'success_story_form': success_story_form,
        'is_share_your_success_story_page_success_message_exists': is_share_your_success_story_page_success_message_exists,
        'is_share_your_success_story_page_error_message_exists': is_share_your_success_story_page_error_message_exists,
    }

    return render(request, 'success_stories/share_your_success_story.html', context=context)



##############################

# PROJECTS PAGE

##############################

def projects(request):

    all_meta_description_objs = ProjectsPageMetaDescription.objects.all()
    all_project_objs = ProjectsPageProject.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_project_objs': all_project_objs,
    }

    return render(request, 'projects/projects.html', context=context)

def project_detail(request, id):

    project_detail = get_object_or_404(ProjectsPageProject, id=id)
    
    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    is_project_detail_page_success_message_exists = False
    is_project_detail_page_error_message_exists = False

    feedback_form = FeedbackForm()

    if request.method == "POST" and "submitBtn" in request.POST:

        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():

            try:

                ProjectDetailPageFeedback.objects.create(
                    project_title=project_detail.title,
                    full_name=feedback_form.cleaned_data['full_name'],
                    email=feedback_form.cleaned_data['email'],
                    phone_number=feedback_form.cleaned_data['phone_number'],
                    feedback=feedback_form.cleaned_data['feedback'],
                    user=user,
                    ip_address=ip,
                    user_agent=user_agent,
                )
                feedback_form = FeedbackForm()
                is_project_detail_page_success_message_exists = True
                info("Feedback has been delivered!")
                messages.success(request, "Your feedback has been delivered!")

            except Exception as e:

                is_project_detail_page_error_message_exists = True
                error(f"Error during feedback giving: {e}")
                messages.error(request, f"An error occurred: {e}")

        else:

            is_project_detail_page_error_message_exists = True
            warning(f"Error with feedback form: {feedback_form.errors}")
            messages.error(request, f'{feedback_form.errors}')

    context = {
        'project_detail': project_detail,
        'feedback_form': feedback_form,
        'is_project_detail_page_error_message_exists': is_project_detail_page_error_message_exists,
        'is_project_detail_page_success_message_exists': is_project_detail_page_success_message_exists,
    }

    return render(request, 'projects/project_detail.html', context=context)



##############################

# CERTIFICATIONS PAGE

##############################

def certifications(request):

    all_meta_description_objs = CertificationsPageMetaDescription.objects.all()
    all_certification_objs = CertificationsPageCertification.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_certification_objs': all_certification_objs,
    }

    return render(request, 'certifications/certifications.html', context=context)



##############################

# RESUME PAGE

##############################

def resume(request):

    all_meta_description = ResumePageMetaDescription.objects.all()
    all_hero_section_objs = ResumePageHeroSection.objects.all()
    all_about_current_position_objs = ResumePageAboutCurrentPosition.objects.all()
    all_experience_objs = ResumePageExperience.objects.all()
    all_education_objs = ResumePageEducation.objects.all()
    all_resume_objs = ResumePageResume.objects.all()

    context = {
        'all_meta_description': all_meta_description,
        'all_hero_section_objs': all_hero_section_objs,
        'all_about_current_position_objs': all_about_current_position_objs,
        'all_experience_objs': all_experience_objs,
        'all_education_objs': all_education_objs,
        'all_resume_objs': all_resume_objs,
    }

    return render(request, 'resume/resume.html', context=context)