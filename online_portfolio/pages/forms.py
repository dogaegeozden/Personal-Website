# LIBRARIES
from django import forms
from django_recaptcha.fields import ReCaptchaField

# MODELS
from .models import ContactPageMessage



# FORM CLASSES

##############################

# CONTACT MESSAGE

##############################

class MessageForm(forms.ModelForm):

    class Meta:

        model = ContactPageMessage

        fields = [
            'full_name',
            'sender_email',
            'phone_num',
            'message',
            'captcha',
        ]

    full_name = forms.CharField(max_length=300, label="Full Name")
    sender_email = forms.EmailField(max_length=300, label="Email")
    phone_num = forms.CharField(max_length=100, required=False, label="Phone Number")
    message = forms.CharField(max_length=10000, label="Message")
    captcha = ReCaptchaField()
