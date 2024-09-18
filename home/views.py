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
    skills = Skill.objects.filter(consultant_id=current_consultant, type=1).order_by("display_order", "label")
    show_skills = False if skills.count() == 0 else True

    tools = Skill.objects.filter(consultant_id=current_consultant, type=2).order_by("display_order", "label")
    show_tools = False if tools.count() == 0 else True

    interests = Skill.objects.filter(consultant_id=current_consultant, type=3).order_by("display_order", "label")
    show_interests = False if interests.count() == 0 else True

    roles = Skill.objects.filter(consultant_id=current_consultant, type=4).order_by("display_order", "label")
    show_roles = False if roles.count() == 0 else True

    pastemployments = PastEmployment.objects.filter(consultant_id=current_consultant)
    show_pastemployments = False if pastemployments.count() == 0 else True

    presslinks = PressLink.objects.filter(consultant_id=current_consultant)
    show_presslinks = False if presslinks.count() == 0 else True

    return render(
        request,
        "home/home.html",
        {"consultant": consultant,
        "skills": skills,
        "show_skills": show_skills,
        "tools": tools,
        "show_tools": show_tools,
        "interests": interests,
        "show_interests": show_interests,
        "roles": roles,
        "show_roles": show_roles,
        "pastemployments": pastemployments,
        "show_pastemployments": show_pastemployments,
        "presslinks": presslinks,
        "show_presslinks": show_presslinks,
        },
    )