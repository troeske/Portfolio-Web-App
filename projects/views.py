from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import Project, Category, Learning, Section, SectionImages, Client
from django.http import HttpResponseRedirect
from home.models import Config
from django.core.mail import send_mail

def get_consultant():
    """
    Get the consultant id from the Config table
    """
    queryset = Config.objects.all()
    consultant = get_object_or_404(queryset, key="CURRENT_CONSULTANT")

    return consultant.value

# Create your views here.

def client_approved(user):
    """
    see if a client/user has been approved
    """
    client = Client.objects.filter(client=user).first()
    if client is None:
        return False
    else:
        return client.approved

def not_in_clients(user):
    """
    see if a client/user is in the client list
    """
    client = Client.objects.filter(client=user).first()
    if client is None:
        return True
    else:
        return False


def projects_list(request):
    """
    Renders the projects home page
    """
    current_consultant = get_consultant()
    
    if request.user.is_authenticated:
        if client_approved(request.user):
            # show all projects
            projects = Project.objects.filter(consultant_id = current_consultant).order_by("display_order", "title")  
        else:
            # show only non-confidential projects
            projects = Project.objects.filter(consultant_id = current_consultant, confidential = False ).order_by("display_order", "title")
    else:
        # show only non-confidential projects
        projects = Project.objects.filter(consultant_id = current_consultant, confidential = False ).order_by("display_order", "title")

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
    # see if the user is approved
    if client_approved(request.user):
        queryset = Project.objects.filter(consultant_id = current_consultant)
    else:
        queryset = Project.objects.filter(consultant_id = current_consultant, confidential = False)
    
    project = get_object_or_404(queryset, slug=slug)

    categories = Category.objects.filter(project_id=project).order_by("display_order", "category")
    show_categories = False if categories.count() == 0 else True
 
    learnings = Learning.objects.filter(project_id=project).order_by("display_order", "header")
    show_learnings = False if learnings.count() == 0 else True

    sections = Section.objects.filter(project_id=project).order_by("display_order", "heading_1")
    show_sections = False if sections.count() == 0 else True

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
def client_registration_list(request):
    """
    CRUD for the client registration list page
    """
    current_consultant = get_consultant()
    
    if request.user.is_superuser:
        # to avoid changing the AllAuth stgandard model we need to add all new the users/clients to the client table 
        users = User.objects.all().order_by("username")
        for a_user in users:
            if a_user.is_superuser:
                client_allow_delete = False
            else:
                client_allow_delete = True
            
            if not_in_clients(a_user):
                new_client = Client(client=a_user, consultant_id=current_consultant, email=a_user.email, allow_delete=client_allow_delete)
                new_client.save()
        
        # now let's get a list of all the clients
        registrations = Client.objects.filter(consultant = current_consultant).order_by( "client","approval_date")
        show_registrations = False if registrations.count() == 0 else True

        return render(
        request,
        "projects/client_registration_list.html",
        {"registrations": registrations,
         "show_registrations": show_registrations
        },
    )
    else:
        # user is not a super user so show nothing to be safe
        show_registrations = False

        return render(
        request,
        "projects/client_registration_list.html",
        {
         "show_registrations": show_registrations
        },

    )

def client_delete(request, username):
    """
    Delete an individual client.

    **Context**

    ``post``
        the client_registration_list.
    ``client``
        A single client.
    """
    
    """ client = Client.objects.get(pk=client_id)
    client.delete()
 """
    # only superusers can delete clients
    if request.user.is_superuser:
        user = User.objects.get(username=username)
        user.delete()

    return HttpResponseRedirect(reverse('client_registration_list'))


def approve_client(request, id):
    """
    Approve a client to view confidential projects.
    """
    # only superusers can approve clients
    if request.user.is_superuser:
        this_client = get_object_or_404(Client, pk=id)
        this_client.approved = True
        this_client.save()
        
        # send email to potential client
        user = User.objects.get(username=this_client.client)
        message = (
            f"Hi {user.username},\n\n"
            "Thanks for registering!\n\n"
            "Your registration was approved\n"
            "\nKind regards"
        )
        
        send_mail(
            "[NO-REPLY] Registration approved",
            message,
            "",
            [this_client.email],
            fail_silently=False,
        )

    return HttpResponseRedirect(reverse('client_registration_list'))
