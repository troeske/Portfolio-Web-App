from django.shortcuts import render, get_object_or_404, reverse
from .models import Consultant, Config, Skill, PastEmployment, PressLink

def get_consultant():
    """
    Get the consultant id from the Config table
    """
    queryset = Config.objects.filter(key="CURRENT_CONSULTANT")
    consultant = get_object_or_404(queryset)
    return consultant.value

# Create your views here.

def consultant_home(request):
    """
    Renders the home page
    """
    consultant = Consultant.objects.filter(id=get_consultant()).first()

    return render(
        request,
        "home/home.html",
        {"consultant": consultant,
        },
    )