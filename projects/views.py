from django.shortcuts import render, get_object_or_404
from .models import Project, Category, Learning, Section, SectionImages
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

def project_details(request, slug):
    """
    Renders the project details page
    """
    current_consultant = get_consultant()
    queryset = Project.objects.filter(consultant_id = current_consultant)
    project = get_object_or_404(queryset, slug=slug)

    categories = Category.objects.filter(project_id=project).order_by("display_order", "category")
    show_categories = False if categories.count() == 0 else True
 
    learnings = Learning.objects.filter(project_id=project).order_by("display_order", "header")
    show_learnings = False if learnings.count() == 0 else True

    sections = Section.objects.filter(project_id=project).order_by("display_order", "heading_1")
    show_sections = False if sections.count() == 0 else True

    # needs to fixed to show only images for the current project !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    images = SectionImages.objects.all().order_by("display_order", "alt_text")
    show_images = False if images.count() == 0 else True
    
    return render(
        request,
        "projects/project_details.html",
        {"project": project,
         "categories": categories,
         "show_categories": show_categories,
         "learnings": learnings,
         "show_learnings": show_learnings,
         "sections": sections,
         "show_sections": show_sections,
         "images": images,
         "show_images": show_images
        },
    )