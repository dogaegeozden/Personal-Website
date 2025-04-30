# MODULES AND LIBRARIES
from django.urls import path
from django.utils.translation import gettext_lazy

# VIEW FUNCTIONS
from .views import (
    success_stories,
    share_your_success_story,
    projects,
    project_detail,
    certifications,
    resume,
)

# URL PATTERS
urlpatterns = [
    path(gettext_lazy('success_stories/'), success_stories, name="success-stories"),
    path(gettext_lazy('share_your_success_story/'), share_your_success_story, name="share-your-success-story"),
    path(gettext_lazy('projects/'), projects, name="projects"),
    path('projects/<uuid:id>', project_detail, name="project-detail"),
    path('projeler/<uuid:id>', project_detail, name="project-detail-translated"),
    path(gettext_lazy('certifications/'), certifications, name="certifications"),
    path(gettext_lazy('resume/'), resume, name="resume")
]
