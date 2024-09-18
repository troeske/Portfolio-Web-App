from django.shortcuts import render, get_object_or_404, reverse
from .models import Consultant, Config

def get_consultant():
    """
    Get the consultant id from the Config table
    """
    consultant = Config.objects.filter(key="CURRENT_CONSULTANT").first()
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