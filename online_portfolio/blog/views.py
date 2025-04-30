# MODULES & LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

# FORMS
from .forms import CommentForm

# MODELS
from .models import (
    BlogPageMetaDescription,
    BlogPageBlogPost,
    BlogPagePostComment,
    BlogPagePostLike,
)

# ONLINE PORTFOLIO FUNCTIONS
from modules.visitor_inspector import (
    get_user,
    get_ip,
    get_user_agent,
)
from modules.logging_config import (
    debug,
    info,
    error,
    warning,
)



##############################

# BLOG PAGE

##############################

def blog(request):

    all_meta_description_objs = BlogPageMetaDescription.objects.all()
    all_blog_post_objs = BlogPageBlogPost.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_blog_post_objs': all_blog_post_objs,
    }

    return render(request, 'blog/blog.html', context=context)

def post_detail_view(request, id):

    post_detail = get_object_or_404(BlogPageBlogPost, id=id)

    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    is_post_detail_page_success_message_exists = False
    is_post_detail_page_error_message_exists = False

    post_like_count = BlogPagePostLike.objects.filter(post=id, like_status='l').count()
    post_like_status = getattr(BlogPagePostLike.objects.filter(post=id, ip_address=ip).last(), 'like_status', None)
    debug(f"Like status: {post_like_status}")
    comment_form = CommentForm()
    number_of_comments = BlogPagePostComment.objects.filter(post=id).count()

    if request.method == "POST" and "likeBtn" in request.POST:

        debug(f"Trying to change the like status to: {request.POST.get('like_changed_to')}")

        if BlogPagePostLike.objects.filter(post=id, ip_address=ip).exists():

            info("Object already exists in the database, modifying it.")
            like_object = BlogPagePostLike.objects.get(post=id, ip_address=ip)
            like_object.like_status = request.POST.get("like_changed_to")
            like_object.save()
            return HttpResponseRedirect(f'/blog/{post_detail.id}')

        else:

            info("Object is not exists in the database so, creating a new one.")
            BlogPagePostLike.objects.create(
                post_id=id,
                ip_address=ip,
                user_agent=user_agent,
                like_status=request.POST.get("like_changed_to"),
            )
            return HttpResponseRedirect(f'/blog/{post_detail.id}')

    elif request.method == "POST" and "commentBtn" in request.POST:

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            try:

                debug(f"Cleaned Form Data = {comment_form.cleaned_data}")
                BlogPagePostComment.objects.create(
                    user=user,
                    text=comment_form.cleaned_data['text'],
                    ip_address=ip,
                    user_agent=user_agent,
                    post_id=post_detail.id,
                )
                is_post_detail_page_success_message_exists = True
                info("Comment has been delivered!")
                messages.success(request, "Your comment has been delivered!")
                return HttpResponseRedirect(f'/blog/{post_detail.id}')

            except Exception as e:

                is_post_detail_page_error_message_exists = True
                error(f"Error during commenting: {e}")
                messages.error(request, f"An error occurred: {e}")

        else:

            is_post_detail_page_error_message_exists = True
            warning(f"Error with comment form: {comment_form.errors}")
            messages.error(request, {comment_form.errors})

    elif request.method == 'POST' and "deleteCommentBtn" in request.POST:

        try:

            BlogPagePostComment.objects.get(id=request.POST.get('comment_id')).delete()
            is_post_detail_page_success_message_exists = True
            info("Comment has been deleted.")
            messages.success(request, "Your comment has been deleted!")
            return HttpResponseRedirect(f'/blog/{post_detail.id}')

        except Exception as e:

            is_post_detail_page_error_message_exists = True
            error(f"Error during comment deletion: {e}")
            messages.error(request, f"An error occurred: {e}")

    context = {
        'is_post_detail_page_success_message_exists': is_post_detail_page_success_message_exists,
        'is_post_detail_page_error_message_exists': is_post_detail_page_error_message_exists,
        'comment_form': comment_form,
        'post_detail': post_detail,
        'post_like_status': post_like_status, 
        'post_like_count': post_like_count,
        'ip_address': ip,
        'number_of_comments': number_of_comments,
    }

    return render(request, 'blog/blog_post_detail.html', context=context)