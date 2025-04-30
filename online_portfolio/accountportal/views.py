# MODULES AND LIBRARIES
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Q

# MODELS
from .models import (
    LoginPageMetaDescription,

    RegisterPageMetaDescription,

    Profile,

    AnnouncementsPageAnnouncement,
    AnnouncementsPageUserAnnouncementView,
)

# ONLINE PORTFOLIO MODULES
from modules.email_sending import send_new_user_email
from modules.random_password import generate_random_password
from modules.logging_config import (
    debug,
    info,
    warning,
    error,
)
from modules.visitor_inspector import (
    get_user,
)
from modules.auth_check import (
    is_admin,
)

# FORMS
from .forms import (
    CustomLoginForm,
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
)

# SETTINGS
from Online_Portfolio.settings import COUNTRY_CHOICES



# VIEW FUNCTIONS

##############################

# LOGIN PAGE

##############################

def custom_login(request):

    if request.user.is_authenticated:

        return redirect('dashboard')

    all_meta_description_objs = LoginPageMetaDescription.objects.all()

    is_login_page_success_message_exists = False
    is_login_page_error_message_exists = False

    login_form = CustomLoginForm()

    if request.method == 'POST' and 'loginBtn' in request.POST:

        login_form = CustomLoginForm(request.POST)

        if login_form.is_valid():

            user = login_form.user  # Retrieved from the form after authentication

            try:

                login(request, user)
                is_login_page_success_message_exists = True
                info(f"User '{user.username}' has been successfully logged in.")

                return redirect('dashboard')

            except Exception as e:

                is_login_page_error_message_exists = True
                logger.error(f"Error during user login: {e}")
                messages.error(request, f"An error occurred: {e}")

        else:

            is_login_page_error_message_exists = True
            warning("Invalid login attempt.")
            messages.error(request, "Login failed. Please check your credentials and CAPTCHA.")

    else:

        login_form = CustomLoginForm()

    context = {
        'login_form': login_form,
        'all_meta_description_objs': all_meta_description_objs,
        'is_login_page_success_message_exists': is_login_page_success_message_exists,
        'is_login_page_error_message_exists': is_login_page_error_message_exists,
    }

    return render(request, 'accountportal/login.html', context)



##############################

# REGISTER PAGE

##############################

def register(request):

    if request.user.is_authenticated:

        return redirect('dashboard')

    is_register_form_success_message_exists = False
    is_register_form_error_message_exists = False

    all_meta_description_objs = RegisterPageMetaDescription.objects.all()

    if request.method == 'POST' and 'registerBtn' in request.POST:

        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():

            if Profile.objects.filter(customer_id=register_form.cleaned_data['username']).exists() == False:

                if User.objects.filter(username=register_form.cleaned_data['username']).exists() == False:

                    if User.objects.filter(email=register_form.cleaned_data['email']).exists() == False:

                        try:

                            new_user = register_form.save()
                            customer_group, created = Group.objects.get_or_create(name='Customers')
                            new_user.groups.add(customer_group)
                            new_user.save()
                            new_user_profile = Profile.objects.get(user_id=new_user.id)
                            random_deliverable_password = generate_random_password()
                            new_user_profile.deliverables_password = random_deliverable_password
                            new_user_profile.save()
                            send_new_user_email(profile=new_user_profile)
                            is_register_form_success_message_exists = True
                            info("User has been registered!.")
                            messages.success(request, "Your account has been created! You are now able to login.")
                            register_form = UserRegisterForm()

                        except Exception as e:

                            is_register_form_error_message_exists = True
                            error(f"Error during user registration: {e}")
                            messages.error(request, f"An error occurred: {e}")

                    else:

                        is_register_form_error_message_exists = True
                        warning("This email address is already in use by another user.")
                        messages.error(request, "This email address is already in use by another user.")

                else:

                    is_register_form_error_message_exists = True
                    warning("This username is already in use by another user.")
                    messages.error(request, "This username is already in use by another user.")

            else:

                is_register_form_error_message_exists = True
                warning("This customer ID is already in use by another user.")
                messages.error(request, "This customer ID is already in use by another user.")

        else:
            
            is_register_form_error_message_exists = True
            warning(f"Error with user register form: {register_form.errors}")
            messages.error(request, f'{register_form.errors}')
    
    else:

        register_form = UserRegisterForm()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'register_form': register_form,
        'is_register_form_success_message_exists': is_register_form_success_message_exists,
        'is_register_form_error_message_exists': is_register_form_error_message_exists,
        'register_form_errors': register_form.errors,
    }

    return render(request, 'accountportal/register.html', context=context)



##############################

# PROFILE PAGE

##############################

@login_required
def profile(request):

    is_profile_page_success_message_exists = False
    is_profile_page_error_message_exists = False

    if request.method == 'POST' and "updateProfileButton" in request.POST:
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
        
            if User.objects.filter(email=u_form.cleaned_data['email']).exclude(id=request.user.id).exists() == False:

                try:

                    u_form.save()
                    p_form.save()
                    is_profile_page_success_message_exists = True
                    info("Account has been updated!")
                    messages.success(request, "Your account has been updated!")

                except Exception as e:

                    is_profile_page_error_message_exists = True
                    error(f"Error during profile update: {e}")
                    messages.error(request, f"An error occurred: {e}")

            else:

                is_profile_page_error_message_exists = True
                warning("Another account is already using this email address.")
                messages.error(request, "Another account is already using this email address.")

        else:

            is_profile_page_error_message_exists = True
            warning(f"Error with user update form: {u_form.errors}")
            warning(f"Error with profile update form: {p_form.errors}")
            messages.error(request, f'{u_form.errors}')
            messages.error(request, f'{p_form.errors}')
            
    elif request.method == 'POST' and "deleteAccountButton" in request.POST:

        try:

            request.user.delete()
            is_profile_page_success_message_exists = True
            info("Account has been deleted!")
            messages.success(request, "Your account has been deleted!")
            return redirect('login')

        except Exception as e:

            is_profile_page_error_message_exists = True
            error(f"Error during account deletion: {e}")
            messages.error(request, f"An error occurred: {e}")

    context = {
        'COUNTRY_CHOICES': COUNTRY_CHOICES,
        'is_profile_page_success_message_exists': is_profile_page_success_message_exists,
        'is_profile_page_error_message_exists': is_profile_page_error_message_exists,
    }

    return render(request, 'accountportal/profile.html', context=context)



##############################

# DASHBOARD PAGE

##############################

@login_required
def dashboard(request):

    # Announcements visible to the user's groups
    user_groups = request.user.groups.all()
    visible_announcements = AnnouncementsPageAnnouncement.objects.filter(
        Q(visible_to_groups__in=user_groups) | Q(visible_to_groups=None)
    ).distinct()

    # Announcements the user has already viewed
    viewed_announcements = AnnouncementsPageUserAnnouncementView.objects.filter(
        user=request.user
    ).values_list('announcement_id', flat=True)

    # Count announcements not yet viewed by the user
    unseen_announcements_count = visible_announcements.exclude(id__in=viewed_announcements).count()


    context = {
        'unseen_announcements_count': unseen_announcements_count,
    }

    return render(request, 'accountportal/dashboard.html', context=context)



##############################

# ANNOUNCEMENTS PAGE

##############################

@login_required
def announcements(request):

    user = get_user(request)

    if is_admin(user):

        all_announcement_objs = AnnouncementsPageAnnouncement.objects.all()

    else:

        all_announcement_objs = AnnouncementsPageAnnouncement.objects.filter(
            visible_to_groups__in=user.groups.all()
        ).distinct()

    # Mark all visible announcements as viewed for the current user
    viewed_announcement_ids = AnnouncementsPageUserAnnouncementView.objects.filter(
        user=user
    ).values_list('announcement_id', flat=True)

    # Get unseen announcements
    unseen_announcements = all_announcement_objs.exclude(id__in=viewed_announcement_ids)

    # Bulk create entries for unseen announcements
    AnnouncementsPageUserAnnouncementView.objects.bulk_create([
        AnnouncementsPageUserAnnouncementView(user=user, announcement=announcement)
        for announcement in unseen_announcements
    ])

    context = {
        'all_announcement_objs': all_announcement_objs,
    }

    return render(request, 'accountportal/announcements.html', context=context)

@login_required
def announcement_detail(request, id):

    announcement_detail = get_object_or_404(AnnouncementsPageAnnouncement, id=id)

    context = {
        "announcement_detail": announcement_detail,
    }

    return render(request, 'accountportal/announcement_detail.html', context=context)