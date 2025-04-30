# MODULES AND LIBRARIES
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField

# MODELS
from django.contrib.auth.models import User
from .models import Profile



# FORMS

##############################

# LOGIN PAGE

##############################

class CustomLoginForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    def clean(self):

        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:

            user = authenticate(username=username, password=password)

            if user is None:

                raise forms.ValidationError("Invalid username or password")

            self.user = user  # Save user for login view

        return cleaned_data



##############################

# USER REGISTER PAGE

##############################

class UserRegisterForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    email = forms.EmailField()
    captcha = ReCaptchaField()



##############################

# USER UPDATE FORM

##############################

class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()

    class Meta:

        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]



##############################

# PROFILE UPDATE FORM

##############################

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        
        model = Profile

        fields = [
            'company_name',
            'phone_number',
            'image',
            'date_of_birth',
            'country',
        ]

    company_name = forms.CharField(max_length=255, required=False,)
    phone_number = forms.CharField(max_length=20, required=False,)
    
    def clean_phone_number(self):
        """
        To validate the phone number before saving it to the database,
        we use a special phone number field for validation.
        If the phone number is not properly set to None when it's left blank,
        saving it to the database will result in an error and
        make it difficult to update profiles without a phone number.
        """

        phone_number = self.cleaned_data['phone_number']
        
        if phone_number in ["None", ""]:
        
            return None
        
        return phone_number
    
    date_of_birth = forms.DateField(required=False,)
    country = forms.CharField(required=False,)