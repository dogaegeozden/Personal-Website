# MODULES AND LIBRARIES
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from email.mime.image import MIMEImage

# ONLINE PORTFOLIO MODELS
from .models import BlogPageBlogPost
from datacenter.models import GlobalSubscription

# ONLINE PORTFOLIO FUNCTIONS
from modules.logging_config import (
    info,
    error,
)

# SETTINGS
from Online_Portfolio.settings import (
    EMAIL_HOST_USER,
)



# SIGNALS

##############################

# BLOG PAGE

##############################

@receiver(post_save, sender=BlogPageBlogPost)
def send_email_on_new_post(sender, instance, created, **kwargs):

    if created:

        subject = f'Check out my latest post: {instance.title}'
        template = 'blog/post_email.html'
        from_email = f'Doga Ege Ozden\'s Blog <{EMAIL_HOST_USER}>'
        subscriptions = GlobalSubscription.objects.all()

        for subscription in subscriptions:
            context = {
                'post': instance,
                'subscription': subscription,
            }

            if instance.image and hasattr(instance.image, 'path'):
                post_image_name = 'post_image'
                context['post_image_name'] = post_image_name

            html_message = render_to_string(template, context)

            email = EmailMessage(
                subject=subject,
                body=html_message,
                from_email=from_email,
                to=[subscription.email],
            )

            if instance.image and hasattr(instance.image, 'path'):
                try:
                    post_image_path = instance.image.path
                    with open(post_image_path, 'rb') as f:
                        post_image_data = f.read()

                    post_image_attachment = MIMEImage(post_image_data, name=post_image_name)
                    post_image_attachment.add_header('Content-ID', f'<{post_image_name}>')
                    post_image_attachment.add_header('Content-Disposition', 'inline', filename=post_image_name)

                    email.attach(post_image_attachment)
                except Exception as e:
                    error(f"Failed to attach image: {e}")

            email.content_subtype = 'html'
            email.send()
            info("Post email has been sent!")