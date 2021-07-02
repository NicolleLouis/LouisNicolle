from django.apps import AppConfig


class ClimaxTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'climax_tracker'

    def ready(self):
        import climax_tracker.signals # noqa
