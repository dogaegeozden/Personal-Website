# LIBRARIES
from django.urls import path
from django.utils.translation import gettext_lazy

# VIEW FUNCTIONS
from .views import (
    home, 
    contact,
    unsubscribe,
    unsubscribe_success,
)

# URL PATTERS
urlpatterns = [
    path('', home, name="home"),
    path(gettext_lazy('contact/'), contact, name="contact"),
    path(gettext_lazy('unsubscribe/success/'), unsubscribe_success, name='unsubscribe_success'),
    path('unsubscribe/<str:token>/', unsubscribe, name='unsubscribe'),
    path('abonelikten_cik/<str:token>/', unsubscribe, name='unsubscribe-translated'),
]