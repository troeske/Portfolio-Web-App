from django.conf import settings
from .models import Config

class LoadConfigMiddleware:
    """
    loads up CSS custom properties from the database
    approach suggested by Github Copilot
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.load_config()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def load_config(self):
        if not hasattr(settings, 'CONTEXT_CONFIG_DATA'):
            settings.CONTEXT_CONFIG_DATA = {}
            configs = Config.objects.filter(consultant_id=1)
            
            # let's load these into a dictionary
            for this_config in configs:
                settings.CONTEXT_CONFIG_DATA[this_config.key] = this_config.value
            