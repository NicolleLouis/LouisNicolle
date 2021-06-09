from django.apps import AppConfig


class AeonConfig(AppConfig):
    name = 'aeon'

    def ready(self):
        import aeon.signals # noqa
