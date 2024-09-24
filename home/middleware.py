from django.conf import settings
from .models import Config

class LoadConfigMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.load_config()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def load_config(self):
        if not hasattr(settings, 'CONFIG_DATA'):
            settings.CONFIG_DATA = {}
            configs = Config.objects.filter(consultant_id=1)
            for this_config in configs:
                settings.CONFIG_DATA[this_config.key] = this_config.value