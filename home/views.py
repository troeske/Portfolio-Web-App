from django.shortcuts import render
from .models import Consultant

# Create your views here.

def consultant_home(request):
    """
    Renders the home page
    """
    consultant = Consultant.objects.all().first()

    return render(
        request,
        "home/home.html",
        {"consultant": consultant},
    )