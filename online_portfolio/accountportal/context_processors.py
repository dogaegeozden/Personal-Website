# DOGA OZDEN CREATIVE STUDIO MODULES
from modules.auth_check import (
    is_admin,
    is_staff,
    is_in_customers_group,
    is_in_customers_group_or_admin,
    is_supervisor_or_admin,
)



# CONTEXT PROCESSORS

##############################

# GROUP INFO PROCESSOR

##############################

def process_group_info(request):
    """
    To make group informations available in every page of this web application.
    So, you can use this data to display different information, to users from 
    different groups.
    """

    has_admin_status = False
    has_staff_status = False
    has_customer_status = False
    has_customer_or_admin_status = False
    has_supervisor_or_admin_status = False

    if request.user.is_authenticated:

        has_admin_status = is_admin(user=request.user)
        has_staff_status = is_staff(user=request.user)
        has_customer_status = is_in_customers_group(user=request.user)
        has_customer_or_admin_status = is_in_customers_group_or_admin(user=request.user)
        has_supervisor_or_admin_status = is_supervisor_or_admin(user=request.user)

    context = {
        'has_admin_status': has_admin_status,
        'has_staff_status': has_staff_status,
        'has_customer_status': has_customer_status,
        'has_customer_or_admin_status': has_customer_or_admin_status,
        'has_supervisor_or_admin_status': has_supervisor_or_admin_status,
    }

    return context
