# LIBRARIES
from django.urls import path
from django.utils.translation import gettext_lazy

# VIEW FUNCTIONS
from .views import (
    blog,
    post_detail_view,
)

# URL PATTERS
urlpatterns = [
    path(gettext_lazy('blog/'), blog, name="blog"),
    path('blog/<uuid:id>', post_detail_view, name="post-detail"),
]