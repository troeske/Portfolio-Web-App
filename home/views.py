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
    current_consultant = get_consultant()
    consultant = Consultant.objects.filter(consultant_id=current_consultant).first()
    skills = Skill.objects.filter(consultant_id=current_consultant, type=1)
    tools = Skill.objects.filter(consultant_id=current_consultant, type=2)
    interests = Skill.objects.filter(consultant_id=current_consultant, type=3)
    roles = Skill.objects.filter(consultant_id=current_consultant, type=4)
    pastemployments = PastEmployment.objects.filter(consultant_id=current_consultant)
    presslinks = PressLink.objects.filter(consultant_id=current_consultant)

    return render(
        request,
        "home/home.html",
        {"consultant": consultant,
        "skills": skills,
        "tools": tools,
        "interests": interests,
        "roles": roles,
        "pastemployments": pastemployments,
        "presslinks": presslinks,
        },
    )