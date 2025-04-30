# ONLINE PORTFOLIO MODULES
from modules.visitor_inspector import (
    get_user,
    get_ip,
    get_user_agent,
)
from modules.data_processing import process_user_data


def collect_user_data(request):
    """
    View to handle user interaction data sent from the frontend.
    """

    ip = get_ip(request)
    user_agent = get_user_agent(request)
    user = get_user(request)

    # Now process user data and return the JSON response
    return process_user_data(request=request, user=user, ip=ip, user_agent=user_agent)