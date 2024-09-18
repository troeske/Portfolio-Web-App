from django.shortcuts import render, get_object_or_404, reverse
from .models import Consultant, Config, Skill, PastEmployment, PressLink

def get_consultant():
    """
    Get the consultant id from the Config table
    """
    queryset = Config.objects.all()
    consultant = get_object_or_404(queryset, key="CURRENT_CONSULTANT")

    return consultant.value

# Create your views here.

def consultant_home(request):
    """
    Renders the home page
    """
    consultant = Consultant.objects.filter(consultant_id=get_consultant()).first()
    
    print(consultant.consultant_id)
    
    return render(
        request,
        "home/home.html",
        {"consultant": consultant,
        },
    )