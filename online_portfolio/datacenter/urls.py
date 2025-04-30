# MODULES AND LIBRARIES
from django.urls import path
from . import views

# URL PATTERNS
urlpatterns = [
    path('collect-user-data/', views.collect_user_data, name='collect_user_data'),
]