# MODELS
from .models import (
    GamesPageGame,
    OpenSourcePageApplication,
    ServicesPageService,
    ApplicationsPageApplication,
)



# CONTEXT PROCESSORS

##############################

# STORE

##############################

def process_product_and_service_number(request):
    """
    To make product and service numbers accessible throughout the web application,
    allowing them to be available on every page.
    """

    number_of_games = GamesPageGame.objects.all().count()
    number_of_services = ServicesPageService.objects.all().count()
    number_of_open_source_application = OpenSourcePageApplication.objects.all().count()
    number_of_application = ApplicationsPageApplication.objects.all().count()

    context = {
        'number_of_games': number_of_games,
        'number_of_services': number_of_services,
        'number_of_open_source_application': number_of_open_source_application,
        'number_of_application': number_of_application,
    }

    return context