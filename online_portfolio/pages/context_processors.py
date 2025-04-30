# MODULES AND LIBRARIES
from django.utils.translation import get_language



# CONTEXT PROCESSORS

##############################

# COOKIE NOTICE

##############################

def process_cookie_notice(request):
    """
    To make the cooke notice answer available throughout the web application,
    so it can be accessible on different pages of the web application, this helps
    in application's decision making, application shows the cookie notice form
    based on cookie notice answer data.
    """

    cookie_notice_answer = request.session.get('cookie_notice_answer', 0)

    if request.method == "POST" and 'iGotIt' in request.POST:

        if cookie_notice_answer <= 1:

            cookie_notice_answer = request.session.get('cookie_notice_answer', 1)
            request.session['cookie_notice_answer'] = cookie_notice_answer + 1
            request.session['cookie_notice_answer'] = cookie_notice_answer + 1

        elif cookie_notice_answer >= 2:

            request.session['cookie_notice_answer'] = cookie_notice_answer

    context = {
        'cookie_notice_answer': cookie_notice_answer,
    }

    return context

def process_languages(request):
    
    context = {
        'language_code': get_language(),
    }

    return context
