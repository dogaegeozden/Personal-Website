# MODULES AND LIBRARIES
from django import forms
from django_recaptcha.fields import ReCaptchaField

# MODELS
from accountportal.models import Profile



# FORMS

##############################

# SERVICES INQUIRY FORM

##############################

class ServiceInquiryForm(forms.ModelForm):

    class Meta:
        
        model = Profile

        fields = [
            'name',
            'email',
            'phone_number',
            'project_details',
        ]

    name = forms.CharField(max_length=255, required=True,)
    email = forms.EmailField(max_length=255, required=True,)
    phone_number = forms.CharField(max_length=100, required=False,)
    project_details = forms.CharField(widget=forms.Textarea, required=True,)
    captcha = ReCaptchaField()