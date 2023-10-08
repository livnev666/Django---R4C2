from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'
    verbose_name = 'Поизводство роботов'

    def ready(self):
        import robots.signals
