# LIBRARIES
from django.core.exceptions import ValidationError



# VALIDATORS

##############################

# FILE SIZE VALIDATOR

##############################

def validate_file_size(value):

    file_size = value.size

    if file_size > 30485760:

        raise ValidationError("The maximum file size that can be uploaded is 30MB")

    else:

        return value