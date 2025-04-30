# MODULES AND LIBRARIES
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from embed_video.fields import EmbedVideoField
from django.core.validators import FileExtensionValidator
from django.utils.translation import get_language
from django.contrib.auth.models import User

# ONLINE PORTFOLIO MODULES
from modules.validators import validate_file_size

# SETTINGS
from Online_Portfolio.settings import (
    LIKE_STATUS_OPTIONS,
)



# DATA CLASSES

##############################

# BLOG PAGE

##############################

class BlogPageMetaDescription(TranslatableModel):

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

        verbose_name_plural = "Blog Page Meta Descriptions"

class BlogPageBlogPost(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier",)
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="Lorem Ipsum",
        help_text=(
            "Write a title for your post.<br><strong>Note: </strong>"
            "<li>Keep it concise and informative</li>"
            "<li>Write for your audience</li><li>Entice the reader</li>"
            "<li>Incorporate important keywords</li><li>Write in sentence case</li>"
        ),
    )

    def upload_post_file(instance, filename):

        current_title = getattr(instance, 'title', 'default_title')

        return f'certification/{current_title}/{filename}'

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_post_file,
        help_text=(
            "<strong>Note: </strong><li>There is no specific required dimension.</li>"
            "<li>Accepted file types are webp, avif, png, jpg and, jpeg.</li>"
            "<li>You can use GIMP to change file type/extension.</li>"
            "<li>Make sure the file size is not over 30MB.</li>"
        ),
        validators=[FileExtensionValidator(['webp', 'avif', 'png', 'jpg', 'jpeg']), validate_file_size],
    )
    video = models.FileField(
        null=True,
        blank=True,
        upload_to=upload_post_file,
        help_text="Upload image or video. This application can't display both. (Prefferred image)",
    )
    youtube_url = EmbedVideoField(
        max_length=1000,
        null=True,
        blank=True,
        help_text=(
            "<strong>Note: </strong><li>Open the video from YouTube. Press to the share > embed. "
            "Only copy paste the url that's 'src' attributes value.</li>"
            "<li><strong>Ex: </strong>'https://www.youtube.com/embed/el1t1FoWdZI'</li>"
            "<li><strong>Hint: Without quotes.</li>"
        ),
    )
    date = models.DateField(
        auto_now_add=False,
        null=True,
        blank=True,
        help_text="Please use the fallowing format: YYYY-MM-DD",
    )
    para1 = models.TextField(
        verbose_name="Paragraph 1",
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        max_length=10000,
        null=False,
        blank=False,
        help_text=(
            "<strong>Notes: </strong>"
            "<li>Unity: Ensure that your paragraph has a central idea or theme. "
            "Every sentence should contribute to or support this main point.</li>"
            "<li>Topic Sentence: Begin the paragraph with a clear and concise topic "
            "sentence that introduces the main idea.</li><li>Coherence: Use logical "
            "transitions between sentences to maintain a smooth flow of ideas. This "
            "helps readers follow your thoughts easily.</li><li>Supporting Details: "
            "Provide specific examples, evidence, or details to support your main "
            "idea. This adds depth and credibility to your paragraph.</li>"
            "<li>Conciseness: Be concise and avoid unnecessary words. Each sentence "
            "should contribute meaningfully to the paragraph.</li><li>Variety in "
            "Sentence Structure: Use a mix of sentence structures – short and long "
            "sentences – to add rhythm and keep the reader engaged.</li><li>Clarity: "
            "Aim for clarity in your writing. Choose words carefully, and ensure that "
            "your sentences are easy to understand.</li><li>Focus: Stick to the main "
            "point of the paragraph. Avoid introducing unrelated ideas that might "
            "confuse the reader.</li><li>Transitions: Use transitional words or "
            "phrases to guide the reader from one idea to the next. This creates "
            "a cohesive and organized paragraph.</li><li>Conclusion: End the "
            "paragraph with a concluding sentence that summarizes the main point "
            "or provides a bridge to the next paragraph.</li>"
        ),
    )
    para2 = models.TextField(verbose_name="Paragraph 2", max_length=10000, null=True, blank=True,)
    para3 = models.TextField(verbose_name="Paragraph 3", max_length=10000, null=True, blank=True,)
    para4 = models.TextField(verbose_name="Paragraph 4", max_length=10000, null=True, blank=True,)
    para5 = models.TextField(verbose_name="Paragraph 5", max_length=10000, null=True, blank=True,)
    para6 = models.TextField(verbose_name="Paragraph 6", max_length=10000, null=True, blank=True,)
    para7 = models.TextField(verbose_name="Paragraph 7", max_length=10000, null=True, blank=True,)
    alt = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Alternative Text",
        help_text=(
            "The alt attribute provides alternative information for an image if a "
            "user for some reason cannot view it (because of slow connection, "
            "an error in the src attribute, or if the user uses a screen reader)."
        ),
    )

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse("post-detail", kwargs={"id": self.id})

    class Meta:

        verbose_name_plural = "Blog Page Posts"
        ordering = ['-date']

class BlogPagePostComment(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name="Universal Unique Identifier",
        help_text="Universal Unique Identifier",
    )
    post = models.ForeignKey(
        'BlogPageBlogPost',
        null=True,
        blank=True,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    text = models.TextField(max_length=1500, null=True, blank=True,)
    comment_time = models.DateTimeField(blank=True, null=True, verbose_name="Comment Time", default=timezone.now,)
    ip_address = models.GenericIPAddressField(null=True, blank=True, default='N/A', verbose_name="Ip Address",)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)

    def __str__(self):

        return f"{self.user.username} - {self.post.title} - {self.comment_time}"

    class Meta:

        verbose_name_plural = "Blog Page Post Comments"
        ordering = ['-comment_time']

class BlogPagePostLike(models.Model):

    post = models.ForeignKey('BlogPageBlogPost', null=True, blank=True, related_name="blogpostlike", on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    like_time = models.DateTimeField(blank=True, null=True, verbose_name="Like Time", default=timezone.now,)
    like_status = models.CharField(
        max_length=1,
        choices=LIKE_STATUS_OPTIONS,
        blank=False,
        default='n',
        verbose_name="Like Status",
    )

    class Meta:

        verbose_name_plural = 'Blog Page Post Like Information'
        ordering = ['-like_time']