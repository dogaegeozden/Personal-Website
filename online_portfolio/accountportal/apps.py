from django.apps import AppConfig

class AccountportalConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountportal'

    def ready(self):
        import accountportal.signals

