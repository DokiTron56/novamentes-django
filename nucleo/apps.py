from django.apps import AppConfig

class NucleoConfig(AppConfig):
    name = 'nucleo'

    def ready(self):
        import config.init_admin
