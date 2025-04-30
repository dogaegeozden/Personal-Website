##############################

# CUSTOMERS AUTH CHECK

##############################

def is_in_customers_group(user):
    """
    To validate if user is in the Customers group.
    Returning True if user is in the Customers group.
    """

    return user.groups.filter(name='Customers').exists()



##############################

# CUSTOMERS OR ADMIN AUTH CHECK

##############################

def is_in_customers_group_or_admin(user):
    """
    To validate if user is in the Customers group or an admin.
    Returning True if user is in the Customers group or a super user.
    """

    return user.groups.filter(name='Customers').exists() or user.is_superuser



##############################

# ADMIN AUTH CHECK

##############################

def is_admin(user):
    """
    To validate if user is a super user.
    Returning True if user is a super user.
    """

    return user.is_superuser



##############################

# STAFF AUTH CHECK

##############################

def is_staff(user):
    """
    To validate if user is a staff.
    Returning True if user is a staff.
    """

    return user.is_staff



##############################

# SUPERVISOR OR ADMIN AUTH CHECK

##############################

def is_supervisor_or_admin(user):

    return user.groups.filter(name="Supervisors") or user.is_superuser