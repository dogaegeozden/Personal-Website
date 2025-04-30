# MODULES AND LIBRARIES
from django.urls import path
from django.utils.translation import gettext_lazy
from django.contrib.auth import views as auth_views

# VIEW FUNCTIONS
from .views import (
    custom_login,
    register,
    profile,
    dashboard,
    announcements,
    announcement_detail,
)

# URL PATTERS
urlpatterns = [
    path(gettext_lazy('dashboard/'), dashboard, name='dashboard'),
    path(gettext_lazy('register/'), register, name='register'),
    path(gettext_lazy('profile/'), profile, name='profile'),
    path(gettext_lazy('login/'), custom_login, name='login'),
    path(
        gettext_lazy('logout/'),
        auth_views.LogoutView.as_view(template_name='accountportal/logged_out.html'),
        name='logout',
    ),
    path(
        gettext_lazy('password_reset/'),
        auth_views.PasswordResetView.as_view(
            template_name='accountportal/password_reset_form.html',
            email_template_name='accountportal/password_reset_email.html',
        ),
        name='password_reset',
    ),
    path(
        gettext_lazy('password_reset/done/'),
        auth_views.PasswordResetDoneView.as_view(template_name='accountportal/password_reset_done.html'),
        name='password_reset_done',
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accountportal/password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    path(
        'sifre_sifirlama_onayi/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accountportal/password_reset_confirm.html'),
        name='password_reset_confirm_translated',
    ),
    path(
        gettext_lazy('password_reset_complete/'),
        auth_views.PasswordResetCompleteView.as_view(template_name='accountportal/password_reset_complete.html'),
        name='password_reset_complete',
    ),
    path(gettext_lazy('announcements/'), announcements, name="announcements"),
    path('announcements/<uuid:id>', announcement_detail, name="announcement-detail"),
    path('duyurular/<uuid:id>', announcement_detail, name="announcement-detail-translated"),
]
