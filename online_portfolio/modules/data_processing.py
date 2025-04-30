# MODULES AND LIBRARIES
from django.http import JsonResponse

# ONLINE PORTFOLIO MODULES
from modules.logging_config import debug

# MODELS
from datacenter.models import (
    GlobalPageVisit,
    GlobalDocumentClickCoordinate,
    GlobalKeystroke,
    GlobalMouseTrace,
    GlobalSocialMediaButtonClick,
    GlobalAppDownloadButtonClick,
)



# DATA PROCESSOR FUNCTIONS

##############################

# PAGE VISIT

##############################

def process_page_visit(request, user, ip, user_agent, screen_width, screen_height, page_url):
    """
    To process and store the details of a page visit.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
        screen_width (int): The user's screen width.
        screen_height (int): The user's screen height.
        page_url (str): The URL of the visited page.
    """

    if request.method == "POST" and request.POST.get("id") == "page_visit_request":
        
        GlobalPageVisit.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            screen_width=screen_width,
            screen_height=screen_height,
            page_url=page_url,
        )



##############################

# DOCUMENT CLICK

##############################

def process_document_click_coordinate(
    request,
    user,
    ip,
    user_agent,
    screen_width,
    screen_height,
    x_coordinate,
    y_coordinate,
    page_url,
):
    """
    To process and store the details of a document click, including coordinates.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
        screen_width (int): The user's screen width.
        screen_height (int): The user's screen height.
        x_coordinate (int): The x-coordinate of the click.
        y_coordinate (int): The y-coordinate of the click.
        page_url (str): The URL of the page where the click occurred.
    """

    if request.method == "POST" and request.POST.get("id") == "document_click_coordinate_request":

        GlobalDocumentClickCoordinate.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            screen_width=screen_width,
            screen_height=screen_height,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            page_url=page_url,
        )



##############################

# KEYSTROKE

##############################

def process_keystroke(request, user, ip, user_agent, keystroke, page_url):
    """
    To process and store the details of a keystroke event.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
        keystroke (str): The key pressed by the user.
        page_url (str): The URL of the page where the keystroke occurred.
    """

    if request.method == "POST" and request.POST.get("id") == "keystroke_request":

        GlobalKeystroke.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            keystroke=keystroke,
            page_url=page_url,
        )



##############################

# MOUSE TRACE

##############################

def process_mouse_trace(
    request,
    user,
    ip,
    user_agent,
    screen_width,
    screen_height,
    x_coordinate,
    y_coordinate,
    page_url
):
    """
    To process and store the details of a mouse trace event.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
        screen_width (int): The user's screen width.
        screen_height (int): The user's screen height.
        x_coordinate (int): The x-coordinate of the mouse.
        y_coordinate (int): The y-coordinate of the mouse.
        page_url (str): The URL of the page where the mouse trace occurred.
    """

    if request.method == "POST" and request.POST.get("id") == "mouse_trace_request":

        GlobalMouseTrace.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            screen_width=screen_width,
            screen_height=screen_height,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            page_url=page_url,
        )



##############################

# SOCIAL MEDIA BUTTON CLICK

##############################

def process_social_media_button_click(request, user, ip, user_agent, platform_choice, page_url):
    """
    To process and store the details of a social media button click.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
        platform_choice (str): The social media platform selected.
        page_url (str): The URL of the page where the click occurred.
    """

    if request.method == "POST" and request.POST.get("id") == "social_media_button_click_request":
 
        GlobalSocialMediaButtonClick.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            platform_choice=platform_choice,
            page_url=page_url,
        )



##############################

# PROCESS USER DATA

##############################

def process_user_data(request, user, ip, user_agent):
    """
    To process user data by calling respective processor functions.

    This function will call each specific data processor function (for page visits, document clicks, keystrokes, etc.)
    based on the data sent in the request. The function will catch any exceptions and log errors.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
    """

    try:

        process_page_visit(
            request=request,
            user=user,
            ip=ip,
            user_agent=user_agent,
            screen_width=request.POST.get("width"),
            screen_height=request.POST.get("height"),
            page_url=request.POST.get("current_url"),
        )
        process_social_media_button_click(
            request=request,
            user=user,
            ip=ip,
            user_agent=user_agent,
            platform_choice=request.POST.get("choice"),
            page_url=request.POST.get("current_url"),
        )
        process_document_click_coordinate(
            request=request,
            user=user,
            ip=ip,
            user_agent=user_agent,
            screen_width=request.POST.get("width"),
            screen_height=request.POST.get("height"),
            x_coordinate=request.POST.get("x_coordinate"),
            y_coordinate=request.POST.get("y_coordinate"),
            page_url=request.POST.get("current_url"),
        )
        process_mouse_trace(
            request=request,
            user=user,
            ip=ip,
            user_agent=user_agent,
            screen_width=request.POST.get("width"),
            screen_height=request.POST.get("height"),
            x_coordinate=request.POST.get("x_coordinate"),
            y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"),
        )
        process_keystroke(
            request=request,
            user=user,
            ip=ip,
            user_agent=user_agent,
            keystroke=request.POST.get("key_value"),
            page_url=request.POST.get("current_url"),
        )

        # Return a JsonResponse on successful processing
        return JsonResponse({'status': 'success', 'message': 'User data processed successfully.'}, status=200)

    except Exception as e:
        
        # Log error and return a failure response
        error(f"Error processing user data: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f"Error processing user data: {str(e)}"}, status=500)



##############################

# PROCESS APP DOWNLOAD CLICKS

##############################

def process_app_download_data(request, user, ip, user_agent):
    """
    To process and store the details of an app download button click.

    Args:
        request (HttpRequest): The HTTP request object.
        user (User): The authenticated user.
        ip (str): The user's IP address.
        user_agent (str): The user's browser user agent.
    """

    if request.method == "POST" and "appDownloadBtn" in request.POST:

        GlobalAppDownloadButtonClick.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            app_choice=request.POST.get("appChoice"),
        )