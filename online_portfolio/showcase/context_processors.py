# MODELS
from .models import (
    SuccessStoriesPageSuccessStory,
    ProjectsPageProject,
    ResumePageExperience,
    CertificationsPageCertification,
)


# CONTEXT PROCESSORS

##############################

# SHOW CASE

##############################

def process_showcase_count(request):

    number_of_success_stories = SuccessStoriesPageSuccessStory.objects.all().count()
    number_of_projects = ProjectsPageProject.objects.all().count()
    number_of_experiences = ResumePageExperience.objects.all().count()
    number_of_certifications = CertificationsPageCertification.objects.all().count()

    context = {
        "number_of_success_stories": number_of_success_stories,
        "number_of_projects": number_of_projects,
        "number_of_experiences": number_of_experiences,
        "number_of_certifications": number_of_certifications,
    }

    return context
