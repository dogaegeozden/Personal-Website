##############################

# IP ADDRESS

##############################

def get_ip(request):
    
    # Try to get the visitor's IP address from the 'X-Forwarded-For' header first
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:

        ip = x_forwarded_for.split(',')[0]

    # Get the visitory's ip address with direct access only
    else:

        ip = request.META.get('REMOTE_ADDR')
        
    return ip



##############################

# USER AGENT

##############################

def get_user_agent(request):

    userAgent = request.META['HTTP_USER_AGENT']
    return userAgent



##############################

# USER

##############################

def get_user(request):
    
    return request.user if not request.user.is_anonymous else None