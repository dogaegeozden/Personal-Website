# MODULES AND LIBRARIES
from django import forms

# MODELS
from .models import GlobalSubscription



# FORM CLASSES

##############################

# SUBSCRIPTION FORM

##############################

class SubscriptionForm(forms.ModelForm):
    
    class Meta:
    
        model = GlobalSubscription

        fields = [
            'email',
        ]

    email = forms.EmailField(max_length=150, label="Email")