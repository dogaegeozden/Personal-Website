# MODULES AND LIBRARIES
from django.core.mail import send_mail
from django.template.loader import render_to_string

# ONLINE PORTFOLIO MODULES
from modules.logging_config import info

# SETTINGS
from Online_Portfolio.settings import (
    EMAIL_HOST_USER,
)



# HELPER FUNCTIONS

##############################

# EMAIL SENDING

##############################

def send_custom_email(subject, message, from_email, recipient_list, template, context):
    """
    To send custom HTML and plain text emails.

    Args:
    - subject (str): The subject of the email.
    - plain_message (str): Plain text message body.
    - from_email (str): The sender's email address.
    - recipient_list (list): A list of email addresses to send the email to.
    - html_template (str): The path to the HTML template.
    - context_data (dict): The context data to be passed to the template for rendering.

    Sends an email with both plain text and HTML parts.
    """

    html_message = render_to_string(template, context)

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
        html_message=html_message,
    )

    info(f"Email has been sent to {', '.join(recipient_list)}.")



# EMAIL SENDING FUNCTIONS

##############################

# NEW USER EMAIL

##############################

def send_new_user_email(profile):
    """
    To send custom emails to new users.

    Args:
    - profile (Profile): New user's profile.
    """

    subject = "Your Account Has Been Created"
    message = "You can login to your account at tamrinotte.com/login/"
    from_email = f"Doga Ege Ozden's Site <{EMAIL_HOST_USER}>"
    recipient_list = [profile.user.email]
    html_message = 'accountportal/new_user_email.html'
    context = {'profile': profile}

    send_custom_email(subject, message, from_email, recipient_list, html_message, context,)