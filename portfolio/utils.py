from django.shortcuts import get_object_or_404
from home.models import Consultant, Config

def get_consultant(config_key_only):
    """
    Get the consultant id from the Config table 
    and first and last name from consultant table
    """
    queryset = Config.objects.all()
    current_consultant = get_object_or_404(queryset, key="CURRENT_CONSULTANT")
    consultant = Consultant.objects.filter(consultant_id=current_consultant.value).first()
    
    if config_key_only:
        return current_consultant.value
    else:
        return current_consultant.value, consultant.first_name, consultant.last_name, consultant.email
