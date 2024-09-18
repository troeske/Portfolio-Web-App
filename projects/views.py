from django.shortcuts import render, get_object_or_404
from .models import Project, Category, Learning, Section
from home.models import Config

def get_consultant():
    """
    Get the consultant id from the Config table
    """
    queryset = Config.objects.all()
    consultant = get_object_or_404(queryset, key="CURRENT_CONSULTANT")

    return consultant.value

# Create your views here.

def projects_list(request):
    """
    Renders the projects home page
    """
    current_consultant = get_consultant()
    projects = Project.objects.filter(consultant_id=current_consultant).order_by("display_order", "title")
    
    show_projects = False if projects.count() == 0 else True
    
    return render(
        request,
        "projects/projects_list.html",
        {"projects": projects,
         "show_projects": show_projects,
        },
    )