# MODULES AND LIBRARIES
from django.contrib import messages

# FORMS
from .forms import SubscriptionForm

# MODELS
from .models import GlobalSubscription

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



# CONTEXT PROCESSORS

##############################

# SUBSCRIPTION FORM

##############################

def process_subscription_form(request):
    
    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    subscription_form = SubscriptionForm()
    is_subscription_form_success_message_exists = False
    is_subscription_form_info_message_exists = False
    is_subscription_form_error_message_exists = False

    if request.method == 'POST' and 'subscribeBtn' in request.POST:

        subscription_form = SubscriptionForm(request.POST)

        if request.method == 'POST':

            if subscription_form.is_valid():

                email = subscription_form.cleaned_data['email']

                if not GlobalSubscription.objects.filter(email=email).exists():

                    try:

                        GlobalSubscription.objects.create(
                            user=user,
                            ip_address=ip,
                            user_agent=user_agent,
                            **subscription_form.cleaned_data,
                        )
                        is_subscription_form_success_message_exists = True
                        info("You successfully subscribed!")
                        messages.success(request, "Thank You!")
                    
                    except Exception as e:

                        is_subscription_form_error_message_exists = True
                        error(f"Something went wrong: {e}")
                        messages.error(request, "Something went wrong. Please try again later.")

                else:

                    is_subscription_form_info_message_exists = True
                    warning("You are already subscribed!")
                    messages.info(request, "You are already subscribed!")

            else:

                is_subscription_form_error_message_exists = True
                debug(subscription_form.errors)
                messages.error(request, f'{subscription_form.errors}')
    
    context = {
        'is_subscription_form_success_message_exists': is_subscription_form_success_message_exists,
        'is_subscription_form_info_message_exists': is_subscription_form_info_message_exists,
        'is_subscription_form_error_message_exists': is_subscription_form_error_message_exists,
    }

    return context