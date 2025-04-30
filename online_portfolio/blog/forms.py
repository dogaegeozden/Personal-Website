# MODULES & LIBRARIES
from django import forms

# MODELS
from .models import BlogPagePostComment



# FORMS

##############################

# COMMENT FORM

##############################

class CommentForm(forms.ModelForm):
    
    class Meta:

        model = BlogPagePostComment

        fields = [
            'text',
        ]

    text = forms.CharField(
        max_length=1500,
        label="Body",
        widget=forms.Textarea(
            attrs={
                'class':'md-textarea form-control',
                'placeholder':'comment here...',
                'rows':'4',
            }
        )
    )
