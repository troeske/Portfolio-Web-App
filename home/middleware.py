from django.conf import settings
from .models import Config, Consultant

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
            CURRENT_CONSULTANT = Config.objects.get(key="CURRENT_CONSULTANT").value
            
            
            # let's add data about the current consultant into the dictionary
            consultant = Consultant.objects.get(consultant_id=CURRENT_CONSULTANT)
            settings.CONTEXT_CONFIG_DATA['consultant_fname'] = consultant.first_name
            settings.CONTEXT_CONFIG_DATA['consultant_lname'] = consultant.last_name
            settings.CONTEXT_CONFIG_DATA['consultant_email'] = consultant.email
            
            # get all config data for the current consultant from the db
            configs = Config.objects.filter(consultant_id=CURRENT_CONSULTANT)
            # let's load these into a dictionary
            for this_config in configs:
                settings.CONTEXT_CONFIG_DATA[this_config.key] = this_config.value
            