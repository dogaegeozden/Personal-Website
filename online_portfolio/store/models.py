# MODULES AND LIBRARIES
from django.db import models
from uuid import uuid4
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db.transaction import atomic
from django.utils.translation import get_language

# ONLINE PORTFOLIO MODULES
from modules.validators import validate_file_size

# MODELS
from accountportal.models import Profile
from django.contrib.auth.models import User

# SETTINGS
from Online_Portfolio.settings import (
    YES_OR_NO_CHOICES,
    EMAIL_HOST_USER,
)



# DATA CLASSES

##############################

# GAMES PAGE

##############################

class GamesPageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=10000,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta:

        verbose_name_plural = "Games Page Meta Descriptions"

class GamesPageGame(TranslatableModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name="ID",
        help_text="Unique ID for this particular game across whole games",
    )
    slug = models.SlugField(
        unique=True,
        max_length=250,
        null=False,
        blank=False,
        help_text="Enter a url path component for your game detail page.",
        default="lorem_ipsum",
    )
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Title",
        default='Lorem Ipsum',
    )

    def generate_game_file_upload_path(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'store/games/{current_title}/{filename}'

    thumbnail_picture = models.ImageField(
        verbose_name="Thumbnail Picture",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=generate_game_file_upload_path,
        help_text=(
            "<strong>Note: </strong><li>Thumbnail pictures must be 500 x 500 px.</li><li>Accepted file types "
            "are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>"
            "<li>Make sure the file "
            "size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    ),
    translations = TranslatedFields(
        meta_description = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and "
                "that's why, you should use sentences which will catch the user's attention."
            ),
        ),
        thumbnail_picture_alt = models.TextField(
            max_length=500,
            null=False,
            blank=False,
            verbose_name="The Main Visual's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it is '
                'indexed by search engines. It\'s good for better search engine optimization.'
            ),
            default="The Game's Main Visual Content",
        ),
        main_image_portrait = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Main Image Portrait",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the main image for mobile devices which is going to be displayed on top of the "
                "page as the main picture.<br><br><strong>Note: </strong><li>Required measurement for the "
                "main promotion image of the game for mobile devices is height/width = 1.35</li><li>Accepted "
                "file types are webp, avif, png, jpg and, jpeg</li><li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        main_image_landscape = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Main Image Landscape",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the main image that is for the tablets and desktops which is going to be displayed "
                "on top of the page as the main picture.<br><br><strong>Note: </strong><li>Required measurement "
                "for the main promotion image of the game for personal computer and tablets is height/width = 1.75"
                "</li><li>Accepted file types are webp, avif, png, jpg and, jpeg</li><li>You can use GIMP to change file "
                "type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        main_visual_alt = models.TextField(
            max_length=500,
            null=False,
            blank=False,
            verbose_name="The Main Visual's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it is '
                'indexed by search engines. It\'s good for better search engine optimization.'
            ),
            default="The Game's Main Visual Content",
        ),
        header1 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 1",),
        image1 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 1",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the first sub image that will be displayed on the main section of the page.<br>"
                "<br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li><li>You can use GIMP "
                "to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt1 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 1's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it is '
                'indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        text1 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 1",),
        header2 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 2",),
        image2 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 2",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the second sub image that will be displayed on the main section of the page.<br>"
                "<br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li><li>You can use GIMP "
                "to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt2 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 2's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it is '
                'indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        text2 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 2",),
        header3 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 3",),
        image3 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 3",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the third sub image that will be displayed on the main section of the page.<br>"
                "<br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li><li>You can use GIMP "
                "to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt3 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 3's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it '
                'is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        text3 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 3",),
        header4 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 4",),
        image4 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 4",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the fourth sub image that will be displayed on the main section of the "
                "page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt4 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 4's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as '
                'it relates to the content of a document or webpage. It is read aloud to users '
                'by screen reader software, and it is indexed by search engines. It\'s good for '
                'better search engine optimization.'
            ),
        ),
        text4 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 4",),
        header5 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 5",),
        image5 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 5",
            upload_to=generate_game_file_upload_path,
            help_text=(
                "This is the fifth sub image that will be displayed on the main section of "
                "the page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt5 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 5's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it '
                'relates to the content of a document or webpage. It is read aloud to users by screen '
                'reader software, and it is indexed by search engines. It\'s good for better search '
                'engine optimization.'
            ),
        ),
        text5 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 5",),
        video1 = models.FileField(
            null=True,
            blank=True,
            upload_to=generate_game_file_upload_path,
            verbose_name="Video 1",
            help_text=(
                "Upload a video. This video will be the first video in the slide show.<br>"
                "<br><strong>Note: </strong><li>Accepted file types are mp4, mov and, avi</li><li>You "
                "can use ShotCut to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['mp4', 'mov', 'avi']), validate_file_size],
        ),
        video2 = models.FileField(
            null=True,
            blank=True,
            upload_to=generate_game_file_upload_path,
            verbose_name="Video 2",
            help_text=(
                "Upload a video. This video will be the second video in the slide show.<br>"
                "<br><strong>Note: </strong><li>Accepted file types are mp4, mov and, avi</li><li>You can "
                "use ShotCut to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['mp4', 'mov', 'avi']), validate_file_size],
        ),
        video3 = models.FileField(
            null=True,
            blank=True,
            upload_to=generate_game_file_upload_path,
            verbose_name="Video 3",
            help_text=(
                "Upload a video. This video will be the third video in the slide show.<br>"
                "<br><strong>Note: </strong><li>Accepted file types are mp4, mov and, avi</li><li>You "
                "can use ShotCut to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['mp4', 'mov', 'avi']), validate_file_size],
        ),
        video4 = models.FileField(
            null=True,
            blank=True,
            upload_to=generate_game_file_upload_path,
            verbose_name="Video 4",
            help_text=(
                "Upload a video. This video will be the fourth video in the slide show.<br><br>"
                "<strong>Note: </strong><li>Accepted file types are mp4, mov and, avi</li><li>You can use ShotCut "
                "to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['mp4', 'mov', 'avi']), validate_file_size],
        ),
        video5 = models.FileField(
            null=True,
            blank=True,
            upload_to=generate_game_file_upload_path,
            verbose_name="Video 5",
            help_text=(
                "Upload a video. This video will be the fifth video in the slide show.<br><br><strong>Note: "
                "</strong><li>Accepted file types are mp4, mov and, avi</li><li>You can use ShotCut to change file "
                "type/extension</li>"
            ),
            validators=[FileExtensionValidator(['mp4', 'mov', 'avi']), validate_file_size],
        ),
        video_alt1 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Video 1's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the content '
                'of a document or webpage. It is read aloud to users by screen reader software, and it is indexed by '
                'search engines. It\'s good for better search engine optimization.'
            ),
        ),
        video_alt2 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Video 2's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the content '
                'of a document or webpage. It is read aloud to users by screen reader software, and it is indexed by '
                'search engines. It\'s good for better search engine optimization.'
            ),
        ),
        video_alt3 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Video 3's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it '
                'is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        video_alt4 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Video 4's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it is '
                'indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        video_alt5 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Video 5's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates to the '
                'content of a document or webpage. It is read aloud to users by screen reader software, and it is '
                'indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
    )
    supported_devices = models.JSONField(
        verbose_name="Supported Devices",
        null=True,
        blank=True,
        default=list,
        help_text=(
            '<p>Enter a list of devices where is application is supported.<br><strong>Ex: </strong>'
            '["Android", "Linux", "Apple", "Windows", "Web"]</p>'
        ),
    )
    coming_soon_status = models.CharField(
        max_length=1,
        choices=YES_OR_NO_CHOICES,
        blank=False,
        null=False,
        default='y',
        help_text=(
            'Decide whether or not if you want upcoming notification span through page which '
            'prevents users from interacting with the particular page'
        ),
        verbose_name="Coming Soon Notification Preview",
    )
    title_preview = models.CharField(
        max_length=1,
        choices=YES_OR_NO_CHOICES,
        blank=False,
        null=False,
        default='y',
        help_text='Decide whether or not if you want to show the title',
        verbose_name="Title Preview",
    )
    google_play_download_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Google Play Store Download Link",
    )
    apple_store_download_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Apple Store Download Link",
    )
    microsoft_store_download_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Microsoft Store Download Link",
    )
    thumbnail_picture = models.ImageField(
        verbose_name="Thumbnail Picture",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=generate_game_file_upload_path,
        help_text=(
            "<strong>Note: </strong><li>Thumbnail pictures must be 500 x 500 px.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change "
            "file type/extension.</li><li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    youtube_url1 = EmbedVideoField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="YouTube URL 1",
        help_text=(
            "Open the video from YouTube. Press share > embed. Only copy paste the "
            "url which is the 'src' attribute's value.<br><br><strong>Ex-url: "
            "</strong>'https://www.youtube.com/embed/el1t1FoWdZI'<br><br>"
            "<strong>Hint: </strong>Enter the url with out quotes."
        ),
    )
    youtube_url2 = EmbedVideoField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="YouTube URL 2",
        help_text=(
            "Open the video from YouTube. Press share > embed. Only copy paste the "
            "url which is the 'src' attribute's value.<br><br><strong>Ex-url: "
            "</strong>'https://www.youtube.com/embed/el1t1FoWdZI'<br><br>"
            "<strong>Hint: </strong>Enter the url with out quotes."
        ),
    )
    youtube_url3 = EmbedVideoField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="YouTube URL 3",
        help_text=(
            "Open the video from YouTube. Press share > embed. Only copy paste "
            "the url which is the 'src' attribute's value.<br><br><strong>Ex-url: </strong>"
            "'https://www.youtube.com/embed/el1t1FoWdZI'<br><br><strong>Hint: </strong>"
            "Enter the url with out quotes."
        ),
    )
    youtube_url4 = EmbedVideoField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="YouTube URL 4",
        help_text=(
            "Open the video from YouTube. Press share > embed. Only copy paste "
            "the url which is the 'src' attribute's value.<br><br><strong>Ex-url: </strong>"
            "'https://www.youtube.com/embed/el1t1FoWdZI'<br><br><strong>Hint: </strong>"
            "Enter the url with out quotes."
        ),
    )
    youtube_url5 = EmbedVideoField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="YouTube URL 5",
        help_text=(
            "Open the video from YouTube. Press share > embed. Only copy paste "
            "the url which is the 'src' attribute's value.<br><br><strong>Ex-url: </strong>"
            "'https://www.youtube.com/embed/el1t1FoWdZI'<br><br><strong>Hint: </strong>"
            "Enter the url with out quotes."
        ),
    )
    posting_time = models.DateField(null=False, blank=False, verbose_name="Posting Time", default=timezone.now,)

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        lang = get_language()

        if lang == "tr":

            return reverse('game-detail-translated', kwargs={"slug": self.slug})

        return reverse('game-detail', kwargs={"slug": self.slug})

    class Meta:

        verbose_name_plural = "Games Page Games"
        ordering = ['-posting_time']



##############################

# OPEN SOURCE PAGE

##############################

class OpenSourcePageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=10000,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )

    class Meta: 

        verbose_name_plural = "Open Source Page Meta Descriptions"

class OpenSourcePageApplication(TranslatableModel):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name="ID",
        help_text="Universal Unique Identifier",
    )
    slug = models.SlugField(
        unique=True,
        max_length=250,
        null=False,
        blank=False,
        help_text="Enter a url path component for your open source application detail page.",
        default="lorem_ipsum",
    )
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Title", default='Lorem Ipsum',)

    def generate_open_source_application_file_upload_path(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'store/open_source_applications/{current_title}/{filename}'

    thumbnail_picture = models.ImageField(
        verbose_name="Thumbnail Picture",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=generate_open_source_application_file_upload_path,
        help_text=(
            "<strong>Note: </strong><li>Thumbnail pictures must be 500 x 500 px.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change file "
            "type/extension.</li><li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    translations = TranslatedFields(
        meta_description = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. "
                "Creating a meta description element is beneficial for better SEO and "
                "that's why, you should use sentences which will catch the user's attention."
            ),
        ),
        introduction_paragraph = models.TextField(
            max_length=10000,
            verbose_name="Introduction Paragraph",
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
        thumbnail_picture_alt = models.TextField(
            verbose_name="Alternative Text for Thumbnail",
            max_length=500,
            null=False,
            blank=False,
            default="Lorem ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if a user "
                "for some reason cannot view it (because of slow connection, an error in the src attribute, "
                "or if the user uses a screen reader)."
            ),
        ),
        header1 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 1",),
        image1 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 1",
            upload_to=generate_open_source_application_file_upload_path,
            help_text=(
                "This is the first sub image that will be displayed on the main section of the "
                "page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt1 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 1's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        text1 = models.TextField(
            max_length=10000,
            null=True,
            blank=True,
            verbose_name="Text 1",
        ),
        header2 = models.CharField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Header 2",
        ),
        image2 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 2",
            upload_to=generate_open_source_application_file_upload_path,
            help_text=(
                "This is the second sub image that will be displayed on the main section of the "
                "page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt2 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 2's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        text2 = models.TextField(max_length=10000, null=True, blank=True, verbose_name="Text 2",),
        header3 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 3",),
        image3 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 3",
            upload_to=generate_open_source_application_file_upload_path,
            help_text=(
                "This is the third sub image that will be displayed on the main section of the "
                "page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, jpeg</li><li>"
                "You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt3 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 3's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
        ),
        text3 = models.TextField(max_length=10000, null=True, blank=True, verbose_name="Text 3",),
    )
    supported_devices = models.JSONField(
        verbose_name="Supported Devices",
        null=True,
        blank=True,
        default=list,
        help_text=(
            '<p>Enter a list of devices where is application is supported.<br><strong>'
            'Ex: </strong>["Android", "Linux", "Apple", "Windows", "Web"]</p>'
        ),
    )
    github_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="GitHub Link",
    )
    posting_time = models.DateField(null=False, blank=False, verbose_name="Posting Time", default=timezone.now,)

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        lang = get_language()

        if lang == "tr":

            return reverse('open-source-app-detail-translated', kwargs={"slug": self.slug})

        return reverse('open-source-app-detail', kwargs={"slug": self.slug})

    class Meta:

        verbose_name_plural = "Open Source Page Applications"
        ordering = ['-posting_time']



##############################

# SERVICES PAGE

##############################

class ServicesPageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        )
    )

    class Meta:

        verbose_name_plural = "Services Page Meta Descriptions"

class ServicesPageMainContent(TranslatableModel):

    translations = TranslatedFields(
        video = models.FileField(
            null=True,
            blank=True,
            upload_to="store/services",
            help_text="Upload image or video. This application can't display both. (Video is preferred)",
        ),
        image = models.ImageField(
            null=True,
            blank=True,
            upload_to="store/services",
            help_text=(
                "<strong>Note: </strong><li>There is no specific required dimension.</li>"
                "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP "
                "to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        alt = models.TextField(
            verbose_name="Alternative Text",
            max_length=500,
            null=False,
            blank=False,
            default="Lorem ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if a user for some "
                "reason cannot view it (because of slow connection, an error in the src attribute, or if the "
                "user uses a screen reader)."
            ),
        ),
        title = models.CharField(
            max_length=300,
            null=False,
            blank=False,
            verbose_name="Title",
            default="Lorem Ipsum",
        ),
        para1 = models.TextField(
            verbose_name="Paragraph 1",
            max_length=10000,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "<strong>How to write a paragraph?</strong><li>Unity: Ensure that your paragraph "
                "has a central idea or theme. Every sentence should contribute to or support this main point.</li>"
                "<li>Topic Sentence: Begin the paragraph with a clear and concise topic sentence that introduces "
                "the main idea.</li><li>Coherence: Use logical transitions between sentences to maintain a smooth "
                "flow of ideas. This helps readers follow your thoughts easily.</li><li>Conciseness: Be concise "
                "and avoid unnecessary words. Each sentence should contribute meaningfully to the paragraph.</li>"
                "<li>Variety in Sentence Structure: Use a mix of sentence structures – short and long sentences – "
                "to add rhythm and keep the reader engaged.</li><li>Clarity: Aim for clarity in your writing. "
                "Choose words carefully, and ensure that your sentences are easy to understand.</li><li>Focus: "
                "Stick to the main point of the paragraph. Avoid introducing unrelated ideas that might confuse "
                "the reader.</li><li>Transitions: Use transitional words or phrases to guide the reader from one "
                "idea to the next. This creates a cohesive and organized paragraph.</li><li>Conclusion: End the "
                "paragraph with a concluding sentence that summarizes the main point or provides a bridge to the "
                "next paragraph.</li>"
            ),
        ),
        para2 = models.TextField(verbose_name="Paragraph 2", max_length=10000, null=True, blank=True,),
        para3 = models.TextField(verbose_name="Paragraph 3", max_length=10000, null=True, blank=True,),
        list_item1 = models.TextField(verbose_name="List Item 1", max_length=1000, null=True, blank=True,),
        list_item2 = models.TextField(verbose_name="List Item 2", max_length=1000, null=True, blank=True,),
        list_item3 = models.TextField(verbose_name="List Item 3", max_length=1000, null=True, blank=True,),
        list_item4 = models.TextField(verbose_name="List Item 4", max_length=1000, null=True, blank=True,),
        list_item5 = models.TextField(verbose_name="List Item 5", max_length=1000, null=True, blank=True,),
        list_item6 = models.TextField(verbose_name="List Item 6", max_length=1000, null=True, blank=True,),
    )

    class Meta:

        verbose_name_plural = "Services Page Main Contents"

class ServicesPageService(TranslatableModel):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    
    def generate_service_file_upload_path(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'store/services/{current_title}/{filename}'

    thumbnail_picture = models.ImageField(
        verbose_name="Thumbnail Picture",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=generate_service_file_upload_path,
        help_text=(
            "<strong>Note: </strong><li>Thumbnail pictures must be 500 x 500 px.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP "
            "to change file type/extension.</li><li>Make sure the file size is not over "
            "30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    translations = TranslatedFields(
        slug = models.SlugField(
            unique=True,
            max_length=250,
            null=False,
            blank=False,
            help_text="Enter a url path component for your service detail page.",
            default="lorem_ipsum",
        ),
        title = models.CharField(
            max_length=255,
            null=False,
            blank=False,
            verbose_name="Title",
            default="Lorem Ipsum",
            help_text=(
                "Write a title for the service that you are providing. "
                "Use a keyword-rich title for better SEO."
            )
        ),
        meta_description = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text="Ensure this description is engaging and includes primary keywords.",
        ),
        call_to_action_sentence = models.TextField(
            max_length=1000,
            null=False,
            blank=False,
            verbose_name="Call to Action",
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
        short_summary = models.TextField(
            max_length=10000,
            null=False,
            blank=False,
            verbose_name="Short Summary",
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "<strong>How to write a paragraph?</strong><li>Unity: Ensure that your paragraph has a "
                "central idea or theme. Every sentence should contribute to or support this main point.</li><li>Topic "
                "Sentence: Begin the paragraph with a clear and concise topic sentence that introduces the "
                "main idea.</li><li>Coherence: Use logical transitions between sentences to maintain a smooth "
                "flow of ideas. This helps readers follow your thoughts easily.</li><li>Conciseness: Be "
                "concise and avoid unnecessary words. Each sentence should contribute meaningfully to the "
                "paragraph.</li><li>Variety in Sentence Structure: Use a mix of sentence structures – short "
                "and long sentences – to add rhythm and keep the reader engaged.</li><li>Clarity: Aim for "
                "clarity in your writing. Choose words carefully, and ensure that your sentences are easy "
                "to understand.</li><li>Focus: Stick to the main point of the paragraph. Avoid introducing "
                "unrelated ideas that might confuse the reader.</li><li>Transitions: Use transitional "
                "words or phrases to guide the reader from one idea to the next. This creates a cohesive and organized "
                "paragraph.</li><li>Conclusion: End the paragraph with a concluding sentence that summarizes the main "
                "point or provides a bridge to the next paragraph.</li>"
            ),
        ),
        thumbnail_pic_alt = models.TextField(
            verbose_name="Alternative Text for The Thumbnail Picture",
            max_length=500,
            null=False,
            blank=False,
            default="Lorem ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if a user for some "
                "reason cannot view it (because of slow connection, an error in the src attribute, or if the "
                "user uses a screen reader)."
            ),
        ),
    )
    posting_time = models.DateField(null=False, blank=False, verbose_name="Posting Time", default=timezone.now,)

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        lang = get_language()

        if lang == "tr":

            return reverse('service-detail-translated', kwargs={"slug": self.slug})

        return reverse('service-detail', kwargs={"slug": self.slug})

    class Meta:

        verbose_name_plural = "Services Page Services"
        ordering = ['-posting_time']

class ServiceDetailPageServiceInclusion(TranslatableModel):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    service = models.ForeignKey(
        'ServicesPageService',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Service",
    )
    translations = TranslatedFields(
        title = models.CharField(
            max_length=255,
            null=False,
            blank=False,
            verbose_name="Title",
            default="Lorem Ipsum",
        ),
        text = models.TextField(
            max_length=10000,
            null=True,
            blank=True,
            verbose_name="Text",
        ),
    )
    create_time = models.DateField(null=False, blank=False, verbose_name="Create Time", default=timezone.now,)

    def __str__(self):

        return f"{self.service.title} - {self.title} - {self.id}"

    class Meta:

        verbose_name_plural = "Service Detail Page Service Inclusions"
        ordering = ['-create_time']

class ServiceDetailPageProcessStep(TranslatableModel):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    step_number = models.IntegerField(null=True, blank=True,)
    service = models.ForeignKey(
        'ServicesPageService',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Service",
    )

    def generate_step_file_upload_path(instance, filename):

        current_title = getattr(instance.service, 'title', 'default_title')

        return f'store/services/{current_title}/{filename}'

    image = models.ImageField(
        verbose_name="Image",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=generate_step_file_upload_path,
        help_text=(
            "<strong>Note: </strong><li>Recommended Dimensions: 500px x 500px.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change "
            "file type/extension.</li><li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )

    translations = TranslatedFields(
        title = models.CharField(
            max_length=255,
            null=False,
            blank=False,
            verbose_name="Title",
            default="Lorem Ipsum",
        ),
        text = models.TextField(
            max_length=10000,
            null=True,
            blank=True,
            verbose_name="Text",
        ),
        list_item_1 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 1",
        ),
        list_item_2 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 2",
        ),
        list_item_3 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 3",
        ),
        list_item_4 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 4",
        ),
        list_item_5 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 5",
        ),
        list_item_6 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 6",
        ),
        list_item_7 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 7",
        ),
        list_item_8 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 8",
        ),
        list_item_9 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 9",
        ),
        list_item_10 = models.TextField(
            max_length=3000,
            null=True,
            blank=True,
            verbose_name="List Item 10",
        ),
        alt = models.TextField(
            verbose_name="Alternative Text",
            max_length=500,
            null=False,
            blank=False,
            default="Lorem ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if "
                "a user for some reason cannot view it (because of slow connection, an error in "
                "the src attribute, or if the user uses a screen reader)."
            ),
        ),
    )
    create_time = models.DateField(null=False, blank=False, verbose_name="Create Time", default=timezone.now,)

    def __str__(self):

        return f'{self.service.title} - Step {self.step_number} - {self.id}'

    class Meta:

        verbose_name_plural = "Service Detail Page Process Steps"
        ordering = ['step_number']

class ServiceDetailPageServiceInquiry(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    service_choice = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="N/A",
        verbose_name="Service Choice",
    )
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Name", default="N/A",)
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name="Email",)
    phone_number = PhoneNumberField(max_length=20, blank=True, null=True, verbose_name="Phone Number",)
    project_details = models.TextField(max_length=255, null=True, blank=True, verbose_name="Project Details",)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    submit_time = models.DateTimeField(blank=True, null=True, verbose_name="Submit Time", default=timezone.now,)

    def send_emails(self):
 
        subject = "Service Inquiry"
        message = "Service Inquiry"
        from_email = f"Doga Ege Ozden Website <{EMAIL_HOST_USER}>"
        to_email = ['dogaegeozden@gmail.com']
        context = {'service_inquiry': self, 'message': message,}
        html_message = render_to_string('services/service_inquiry_email.html', context)

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
            html_message=html_message,
        )

    class Meta:
        
        verbose_name_plural = 'Service Detail Page Service Inquiries'
        ordering = ['-submit_time']



##############################

# APPLICATIONS PAGE

##############################

class ApplicationsPageMetaDescription(TranslatableModel):

    translations = TranslatedFields(
        text = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
    )
    class Meta: 

        verbose_name_plural = "Applications Page Meta Descriptions"

class ApplicationsPageApplication(TranslatableModel):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    slug = models.SlugField(
        unique=True,
        max_length=250,
        null=False,
        blank=False,
        help_text="Enter a url path component for your application detail page.",
        default="lorem_ipsum",
    )
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Title",
        default='Lorem Ipsum',
    )
    supported_devices = models.JSONField(
        verbose_name="Supported Devices",
        null=True,
        blank=True,
        default=list,
        help_text=(
            '<p>Enter a list of devices where is application is supported.<br><strong>Ex: '
            '</strong>["Android", "Linux", "Apple", "Windows", "Web"]</p>'
        ),
    )

    def generate_application_file_upload_path(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'store/applications/{current_title}/{filename}'

    thumbnail_picture = models.ImageField(
        verbose_name="Thumbnail Picture",
        default="defaults/default.jpg",
        null=False,
        blank=False,
        upload_to=generate_application_file_upload_path,
        help_text=(
            "<strong>Note: </strong><li>Thumbnail pictures must be 500 x 500 px.</li><li>"
            "Accepted file types are webp, avif, png, jpg and, jpeg.</li><li>You can use GIMP to change file "
            "type/extension.</li><li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )

    translations = TranslatedFields(
        meta_description = models.TextField(
            max_length=1500,
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            help_text=(
                "Meta description is a HTML element that describes the page's content. Creating a "
                "meta description element is beneficial for better SEO and that's why, you should use sentences "
                "which will catch the user's attention."
            ),
        ),
        thumbnail_picture_alt = models.TextField(
            verbose_name="Alternative Text for Thumbnail",
            max_length=500,
            null=False,
            blank=False,
            default="Lorem ipsum",
            help_text=(
                "The alt attribute provides alternative information for an image if a user "
                "for some reason cannot view it (because of slow connection, an error in the src attribute, "
                "or if the user uses a screen reader)."
            ),
        ),
        main_visual_portrait = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Main Visual Portrait",
            upload_to=generate_application_file_upload_path,
            help_text=(
                "This is the main feature graphic image for mobile devices which is going to "
                "be displayed on top of the page as the main picture.<br><br><strong>Note: </strong><li>"
                "Required measurement for the main promotion image of the game for mobile devices is "
                "height/width = 1.35</li><li>Accepted file types are webp, avif, png, jpg and, jpeg</li><li>You can "
                "use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        main_visual_landscape = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Main Visual Landscape",
            upload_to=generate_application_file_upload_path,
            help_text=(
                "This is the main image that is for the tablets and desktops which is going to "
                "be displayed on top of the page as the main picture.<br><br><strong>Note: </strong><li>"
                "Required measurement for the main promotion image of the game for personal computer and "
                "tablets is height/width = 1.75</li><li>Accepted file types are webp, avif, png, jpg and, jpeg</li>"
                "<li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        main_visual_alt = models.TextField(
            max_length=500,
            null=False,
            blank=False,
            verbose_name="Alternative Text for The Main Visual",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it relates '
                'to the content of a document or webpage. It is read aloud to users by screen reader software, '
                'and it is indexed by search engines. It\'s good for better search engine optimization.'
            ),
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
        introduction_paragraph = models.TextField(
            max_length=10000,
            verbose_name="Introduction Paragraph",
            null=False,
            blank=False,
            default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        ),
        header1 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 1",),
        text1 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 1",),
        image1 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 1",
            upload_to=generate_application_file_upload_path,
            help_text=(
                "This is the first sub image that will be displayed on the main section of "
                "the page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, "
                "jpeg</li><li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt1 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 1's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it '
                'relates to the content of a document or webpage. It is read aloud to users by screen '
                'reader software, and it is indexed by search engines. It\'s good for better search '
                'engine optimization.'
            ),
        ),
        header2 = models.CharField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Header 2",
        ),
        image2 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 2",
            upload_to=generate_application_file_upload_path,
            help_text=(
                "This is the second sub image that will be displayed on the main section "
                "of the page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, "
                "jpeg</li><li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt2 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 2's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it '
                'relates to the content of a document or webpage. It is read aloud to users by screen '
                'reader software, and it is indexed by search engines. It\'s good for better search '
                'engine optimization.'
            ),
        ),
        text2 = models.TextField(max_length=500, null=True, blank=True, verbose_name="Text 2",),
        header3 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Header 3",),
        image3 = models.ImageField(
            null=True,
            blank=True,
            verbose_name="Image 3",
            upload_to=generate_application_file_upload_path,
            help_text=(
                "This is the third sub image that will be displayed on the main section of "
                "the page.<br><br><strong>Note: </strong><li>Accepted file types are webp, avif, png, jpg and, "
                "jpeg</li><li>You can use GIMP to change file type/extension</li>"
            ),
            validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
        ),
        image_alt3 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Image 3's Alternative Text",
            help_text=(
                'Alternative (Alt) Text is meant to convey the "why" of the image as it '
                'relates to the content of a document or webpage. It is read aloud to users by screen '
                'reader software, and it is indexed by search engines. It\'s good for better search '
                'engine optimization.'
            ),
        ),
        text3 = models.TextField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name="Text 3",
        ),
    )
    google_play_download_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Google Play Store Download Link",
    )
    apple_store_download_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Apple Store Download Link",
    )
    microsoft_store_download_link = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Microsoft Store Download Link",
    )
    price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=2,
    )
    posting_time = models.DateField(
        null=False,
        blank=False,
        verbose_name="Posting Time",
        default=timezone.now,
    )

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        lang = get_language()

        if lang == "tr":

            return reverse('application-detail-translated', kwargs={"slug": self.slug})

        return reverse('application-detail', kwargs={"slug": self.slug})

    class Meta:

        verbose_name_plural = "Applications Page Applications"
        ordering = ['-posting_time']