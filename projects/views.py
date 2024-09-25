from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import Project, Category, Learning, Section, SectionImages, Client
from django.http import HttpResponseRedirect
from portfolio.utils import get_consultant
from django.core.mail import send_mail
from django.http import HttpResponse
from django.db import DatabaseError
from .utils import client_approved, not_in_clients
from django.conf import settings

# Create your views here.

def projects_list(request):
    """
    Renders the projects home page
    """
    
    try:
        current_consultant = get_consultant(True)
        
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
    
    except Exception as e:
        error_message = f"A general error occurred:: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
    context = {"projects": projects,
                "show_projects": show_projects,
               }

    # let's append the config data for CSS custom properties to the context dictionary
    context.update(settings.CONTEXT_CONFIG_DATA)
    
    return render(
        request,
        "projects/projects_list.html",
        context,
        )

def project_details(request, slug):
    """
    Renders the project details page
    """
    try:
        current_consultant = get_consultant(True)
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
    
    except Exception as e:
        error_message = f"A general error occurred:: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
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

    current_consultant = get_consultant(True)
    
    if request.user.is_superuser:
        try:
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

        except Exception as e:
            error_message = f"A general error occurred:: {e}. Please try again later."
            print(error_message)
            print(type(e))
            return HttpResponse(error_message, status=500)  
    
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

    try:
        # only superusers can delete clients
        if request.user.is_superuser:
            user = User.objects.get(username=username)
            user.delete()
    
    except DatabaseError as e:
               error_message = f"A Database error occurred: {e}. Please try again later."
               print(error_message)
               print(type(e))
               return HttpResponse(error_message, status=500)
    
    except Exception as e:
        error_message = f"A general error occurred:: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
    return HttpResponseRedirect(reverse('client_registration_list'))


def approve_client(request, id):
    """
    Approve a client to view confidential projects.
    """
    try:
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
    
    except DatabaseError as e:
        error_message = f"A Database error occurred: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)

    except Exception as e:
        error_message = f"A general error occurred:: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
    return HttpResponseRedirect(reverse('client_registration_list'))
