# MODULES AND LIBRARIES
from django import forms
from django_recaptcha.fields import ReCaptchaField

# MODELS
from .models import (
    SuccessStoriesPageSuccessStory,
    ProjectDetailPageFeedback,
)



# FORMS

##############################

# SUCCESS STORIES PAGE

##############################

class SuccessStoryForm(forms.ModelForm):

    class Meta:
        
        model = SuccessStoriesPageSuccessStory

        fields = [
            'job_title',
            'website_link',
            'text',
        ]

    job_title = forms.CharField(max_length=500, required=True)
    website_link = forms.URLField(label="Website", required=False)
    text = forms.CharField(label="Description", required=True)
    captcha = ReCaptchaField()


##############################

# PROJECTS PAGE

##############################

class FeedbackForm(forms.ModelForm):

    class Meta:
        
        model = ProjectDetailPageFeedback

        fields = [
            'full_name',
            'email',
            'phone_number',
            'feedback',
            'captcha',
        ]

    full_name = forms.CharField(max_length=300, label="Full Name")
    email = forms.EmailField(max_length=300, label="Email")
    phone_number = forms.CharField(max_length=100, required=False, label="Phone Number")
    feedback = forms.CharField(max_length=10000, label="Feed Back")
    captcha = ReCaptchaField()
