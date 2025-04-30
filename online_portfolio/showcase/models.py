# MODULES AND LIBRARIES
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import FileExtensionValidator
from django.utils.translation import get_language

# MODELS
from django.contrib.auth.models import User

# ONLINE PORTFOLIO MODULES
from modules.validators import validate_file_size

# SETTINGS
from Online_Portfolio.settings import (
    EMAIL_HOST_USER,
    WORK_STATUS_CHOICES,
)



# DATA CLASSES

##############################

# SUCCESS STORIES

##############################

class SuccessStoriesPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. Creating a meta "
                "description element is beneficial for better SEO and that's why, you should use sentences "
                "which will catch the user's attention."
            ),
        ),
    )
    
    class Meta:

        verbose_name_plural = "Success Stories Page Meta Descriptions"

class SuccessStoriesPageSuccessStory(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name="Universal Unique Identifier",
        help_text="Universal Unique Identifier",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="User",)
    job_title = models.CharField(
        verbose_name="Job Title",
        max_length=250,
        null=False,
        blank=False,
        default="Lorem Ipsum",
    )
    website_link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Website Link",) 
    text = models.TextField(
        max_length=10000,
        null=False,
        blank=False,
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    )
    posting_time = models.DateTimeField(blank=False, null=False, verbose_name="Posting Time", default=timezone.now)
    ip_address = models.GenericIPAddressField(null=False, blank=False, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=1000, null=True, blank=True, verbose_name="User Agent", default="N/A",)

    class Meta:

        verbose_name_plural = "Success Stories Page Success Stories"
        ordering = ['-posting_time']



##############################

# PROJECTS

##############################

class ProjectsPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and that's why, "
                "you should use sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Projects Page Meta Descriptions"

class ProjectsPageProject(TranslatableModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name="Universal Unique Identifier",
        help_text="Universal Unique Identifier",
    )

    def upload_project_picture(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'projects/{current_title}/{filename}'

    client = models.CharField(verbose_name="Client", null=True, blank=True, max_length=250, default="Lorem Ipsum",)
    tags = models.JSONField(
        verbose_name="Tags",
        null=True,
        blank=True,
        default=list,
        help_text=(
            '<p>Enter project tags using python list syntax.<br><strong>Ex: </strong>'
            '["WordPress", "MySQL", "Elementor", "HTML", "CSS", "JavaScript", "PHP"]</p>'
        ),
    )
    url = models.URLField(max_length=200, verbose_name="URL",)
    thumbnail_picture = models.ImageField(
        verbose_name="Thumbnail Picture",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=upload_project_picture,
        help_text=(
            "<strong>Note: </strong><li>Thumbnail pictures must be 500 x 500 px.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change" 
            "file type/extension.</li><li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture1 = models.ImageField(
        verbose_name="Project Picture 1",
        null=False,
        blank=False,
        upload_to=upload_project_picture,
        default="defaults/default.jpg",
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg "
            "and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture2 = models.ImageField(
        verbose_name="Project Picture 2",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg "
            "and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture3 = models.ImageField(
        verbose_name="Project Picture 3",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg "
            "and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture4 = models.ImageField(
        verbose_name="Project Picture 4",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure all "
            "images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg and, "
            "jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture5 = models.ImageField(
        verbose_name="Project Picture 5",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure all "
            "images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg and, "
            "jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture6 = models.ImageField(
        verbose_name="Project Picture 6",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg and, "
            "jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture7 = models.ImageField(
        verbose_name="Project Picture 7",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg "
            "and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture8 = models.ImageField(
        verbose_name="Project Picture 8",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg "
            "and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    picture9 = models.ImageField(
        verbose_name="Project Picture 9",
        null=True,
        blank=True,
        upload_to=upload_project_picture,
        help_text=(
            "Don't forget to retouch to your project pictures before publishing them.<br>"
            "<br><strong>Note: </strong><li>There is no speicifc dimension requirement but make sure "
            "all images are in same size for same project.</li><li>Accepted file types are webp, avif, png, jpg and, "
            "jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    upload_time = models.DateTimeField(blank=False, null=False, verbose_name="Upload Time", default=timezone.now,)
    translations = TranslatedFields(
        title = models.CharField(verbose_name="Title", null=True, blank=True, max_length=250, default="Lorem Ipsum",),
        meta_description = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and that's why, you "
                "should use sentences which will catch the user's attention."
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
        project_type = models.CharField(
            verbose_name="Project Type",
            null=True,
            blank=True,
            max_length=250,
            default="Lorem Ipsum",
        ),
        description = models.TextField(
            max_length=10000,
            null=False,
            blank=False,
            help_text="Write a description for the project you are planning to share.",
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
        thumbnail_picture_alt = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            verbose_name="Alternative Text for Thumbnail Picture",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it '
                'relates to the content of a document or webpage. It is read aloud to users by screen '
                'reader software, and it is indexed by search engines. It\'s good for better search '
                'engine optimization.'
            ),
        ),
        alt1 = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            verbose_name="Alternative Text 1",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt2 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 2",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt3 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 3",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt4 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 4",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt5 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 5",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt6 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 6",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt7 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 7",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt8 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 8",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to '
                'the content of a document or webpage. It is read aloud to users by screen reader software, and '
                'it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt9 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 9",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as '
                'it relates to the content of a document or webpage. It is read aloud to users by '
                'screen reader software, and it is indexed by search engines. It\'s good for '
                'better search engine optimization.'
            ),
        ),
    )

    def __str__(self):

        return f'{self.title}'

    def get_absolute_url(self):
    
        lang = get_language()

        if lang == "tr":
    
            return reverse("project-detail-translated", kwargs={"id": self.pk})

        return reverse("project-detail", kwargs={"id": self.pk})

    class Meta:

        verbose_name_plural = "Projects Page Projects"
        ordering = ['-upload_time']

class ProjectDetailPageFeedback(models.Model):

    project_title = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        default="N/A",
        verbose_name="Project Title",
    )
    full_name = models.CharField(max_length=300, null=False, blank=False, default="N/A", verbose_name="Full Name",)
    email = models.EmailField(max_length=300, null=False, blank=False, default="N/A", verbose_name="Email",)
    phone_number = PhoneNumberField(max_length=20, blank=True, null=True, verbose_name="Phone Number",)
    feedback = models.TextField(max_length=10000, null=False, blank=False, default="N/A", verbose_name="Feedback",)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User",)
    ip_address = models.GenericIPAddressField(null=False, blank=False, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=1000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    sending_time = models.DateTimeField(blank=False, null=False, verbose_name="Send Time", default=timezone.now,)

    def send_emails(self):

        subject = "New Feedback"
        message = "New Feedback"
        from_email = f"Doga Ege Ozden's Site<{EMAIL_HOST_USER}>"
        to_email = ['dogaegeozden@gmail.com']
        html_message = render_to_string('projects/feedback_email.html', {'feedback': self, 'message': message,})

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
            html_message=html_message,
        )

    class Meta:

        verbose_name_plural = "Project Detail Page Feedback"



##############################

# RESUMES PAGE

##############################

class ResumePageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and that's why, "
                "you should use sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Resume Page Meta Descriptions"

class ResumePageHeroSection(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(
            max_length=250,
            blank=False,
            null=False,
            default="Lorem Ipsum",
        ),
        image = models.ImageField(
            null=False,
            blank=False,
            default="defaults/default.jpg",
            upload_to='home/hero_section',
            help_text=(
                "<strong>Note: </strong><li>Dimension requirement is 1.3 height/width</li>"
                "<li>Don't forget to scale down your images to increase load speed.</li>"
                "<li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change the file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        text = models.TextField(
            max_length=10000,
            blank=False,
            null=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "<strong>Notes: </strong>"
                "<li>Introduce your self.</li>"
                "<li>Include the most relevant professional experience.</li>"
                "<li>Mention significant personal achievements or awards.</li>"
                "<li>Introduce personal details.</li><li>Use a casual and friendly tone.</li>"
            ),
        ),
        alt = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as '
                'it relates to the content of a document or webpage. It is read aloud '
                'to users by screen reader software, and it is indexed by search engines. '
                'It\'s good for better search engine optimization.'
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Resume Page Hero Sections"

class ResumePageAboutCurrentPosition(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=3000,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Explain what are dealing with currently as the third person.<br>"
                "<strong>Ex: </strong>A self taught programmer seeking for a full "
                "time position, where he can utilize his skills and knowledge "
                "in web development field."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Resume Page About Current Positions"

class ResumePageResume(models.Model):

    field_name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name="Field Name",
        default="Lorem Ipsum",
        help_text="Write the name of the field which you prepared resume for.",
    )
    resume_name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name="Resume Name",
        default="Lorem Ipsum",
        help_text="Give your resume a name.<br><strong>Note: </strong>This name will be used to name the object.",
    )

    def upload_resume_file(instance, filename):

        current_field_name = getattr(instance, 'field_name', 'default_field_name')

        return f'resumes/{current_field_name}/{filename}'

    file = models.FileField(
        null=False,
        blank=False,
        default="/defaults/resume_dogaegeozden_full_stack_web_developer.pdf",
        upload_to=upload_resume_file,
        help_text=(
            "<strong>Note: </strong>"
            "<li>There is no specific required dimension.</li><li>Accepted file type is pdf.</li>"
            "<li>You can use the Libre Writer to convert word files to pdf files.</li>"
            "<li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['pdf']), validate_file_size],
    )

    def __str__(self):

        return f"{self.field_name} - {self.resume_name}"

    class Meta:

        verbose_name_plural = "Resume Page Resumes"

class ResumePageExperience(TranslatableModel):

    translations = TranslatedFields(
        job_title = models.CharField(
            max_length=300,
            null=False,
            blank=False,
            verbose_name="Job Title",
            default="Lorem Ipsum",
            help_text="Write the job title of your experience.",
        ),
        company_name = models.CharField(
            max_length=300,
            null=False,
            blank=False,
            verbose_name="Company Name",
            default="Lorem Ipsum",
            help_text="Write the name of the company that you worked for.",
        ),
        text = models.TextField(max_length=550, blank=True, null=True, help_text="Write a short job description."),
        header = models.CharField(
            max_length=200,
            null=True,
            blank=True,
            help_text="Write a header which will be located on top of the list item. Ex: Summary",
        ),
        list_item_1 = models.CharField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="List Item 1",
            help_text="Write a task that you completed during your experience.",
        ),
        list_item_2 = models.CharField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="List Item 2",
            help_text="Write a task that you completed during your experience.",
        ),
        list_item_3 = models.CharField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="List Item 3",
            help_text="Write a task that you completed during your experience.",
        ),
        list_item_4 = models.CharField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="List Item 4",
            help_text="Write a task that you completed during your experience.",
        ),
        list_item_5 = models.CharField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="List Item 5",
            help_text="Write a task that you completed during your experience.",
        ),
        alt1 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 1",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt2 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 2",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt3 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 3",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt4 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 4",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt5 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 5",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        alt6 = models.TextField(
            max_length=1000,
            null=True,
            blank=True,
            verbose_name="Alternative Text 6",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
    )

    def upload_experience_file(instance, filename):

        current_title = getattr(instance, 'job_title', 'default_title')

        return f'experiences/{current_title}/{filename}'

    img1 = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_experience_file,
        verbose_name="Experince Picture 1",
        help_text=(
            "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP "
            "to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    img2 = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_experience_file,
        verbose_name="Experince Picture 2",
        help_text=(
            "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li>"
            "<li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    img3 = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_experience_file,
        verbose_name="Experince Picture 3",
        help_text=(
            "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li>"
            "<li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    img4 = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_experience_file,
        verbose_name="Experince Picture 4",
        help_text=(
            "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP "
            "to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    img5 = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_experience_file,
        verbose_name="Experince Picture 5",
        help_text=(
            "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li>"
            "<li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    img6 = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_experience_file,
        verbose_name="Experince Picture 6",
        help_text=(
            "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li>"
            "<li>You can use GIMP to change file type/extension.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    working_status = models.CharField(
        max_length=1,
        choices=WORK_STATUS_CHOICES,
        blank=False,
        null=False,
        default='n',
        help_text='Working status', 
        verbose_name="Working Status",
    )
    start_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Start Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )
    end_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="End Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )

    class Meta:

        verbose_name_plural = "Resume Page Experiences"
   
    def __str__(self):

        return self.job_title

class ResumePageEducation(TranslatableModel):

    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="School Name",
    )
    city = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    province = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    start_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Start Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )
    end_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="End Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )

    translations = TranslatedFields(
        major = models.CharField(
            max_length=300,
            null=False,
            blank=False,
            verbose_name="Major",
            default="Lorem Ipsum",
        ),
        diploma = models.TextField(
            max_length=300,
            null=True,
            blank=True,
            verbose_name="Diploma",
            default="Lorem Ipsum",
        ),
        para = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="Paragraph",
        ),
        img = models.ImageField(
            null=True,
            blank=True,
            upload_to="Education",
            verbose_name="Image",
            help_text=(
                "<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li>"
                "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li>"
                "<li>You can use GIMP to change file type/extension.</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
    )

    class Meta:

        verbose_name_plural = "Resume Page Educations"
    
    def __str__(self):

        return self.name



##############################

# CERTIFICATIONS PAGE

##############################

class CertificationsPageMetaDescription(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and that's why, "
                "you should use sentences which will catch the user's attention."
            ),
        ),
    )

    class Meta:

        verbose_name_plural = "Certifications Page Meta Descriptions"

class CertificationsPageCertification(models.Model):
    
    def upload_certification_file(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'certification/{current_title}/{filename}'

    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        default="Lorem Ipsum",
        help_text=(
            "Write the title of your certification.<br>"
            "<strong>Hint: </strong>You can simply write the name of the certification."
        ),
    )
    topic = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        default="Lorem Ipsum",
        help_text="Write a topic which categorizes your application.<br><strong>Ex: </strong>Microsoft Office",
    )
    digital_copy = models.FileField(
        verbose_name="Digital Copy",
        null=True,
        blank=True,
        upload_to=upload_certification_file,
        help_text=(
            "<strong>Note: </strong><li>There is no specific required dimension.</li>"
            "<li>Accepted file types are webp, avif, pdf, png, jpg and, jpeg.</li>"
            "<li>You can use GIMP to change file type/extension.</li>"
            "<li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'pdf', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    digital_copy_url = models.URLField(
        verbose_name="URL of The Certification",
        null=True,
        blank=True,
        help_text="Add a URL leading to your certification if you don't have a digital copy.",
        max_length=255,
    )
    issuer = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        default="Lorem Ipsum",
        help_text="Write the name of the organization who issued this certification.",
    )
    issue_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Issue Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )
    expiry_date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Expiry Date",
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )

    class Meta:

        verbose_name_plural = "Certifications Page Certifications"

    def __str__(self):

        return self.title