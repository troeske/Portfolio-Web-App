from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Project, Category, Learning, Section
from .models import SectionImages, Client, SectionVideo
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.db import DatabaseError
from .utils import client_approved, not_in_clients
from django.conf import settings


def projects_list(request):
    """
    Renders the projects home page
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        if request.user.is_authenticated:
            if client_approved(request.user):
                # show all projects
                projects = Project.objects.filter(
                    consultant_id=current_consultant).order_by(
                    "display_order", "title"
                )
            else:
                # show only non-confidential projects
                projects = Project.objects.filter(
                    consultant_id=current_consultant, confidential=False
                ).order_by("display_order", "title")
        else:
            # show only non-confidential projects
            projects = Project.objects.filter(
                consultant_id=current_consultant, confidential=False
            ).order_by("display_order", "title")

        show_projects = projects.exists()

    except Exception as e:
        error_message = f"A general error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    context = {
        "projects": projects,
        "show_projects": show_projects
    }

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
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        # see if the user is approved
        if client_approved(request.user):
            queryset = Project.objects.filter(consultant_id=current_consultant)
        else:
            queryset = Project.objects.filter(
                consultant_id=current_consultant, confidential=False
            )

        project = get_object_or_404(queryset, slug=slug)

        categories = Category.objects.filter(project_id=project).order_by(
            "display_order", "category"
        )
        show_categories = categories.exists()

        learnings = Learning.objects.filter(project_id=project).order_by(
            "display_order", "header"
        )
        show_learnings = learnings.exists()

        sections = Section.objects.filter(project_id=project).order_by(
            "display_order", "heading_1"
        )
        show_sections = sections.exists()

        # calculate the number of images per section for the image carousel
        section_image_counts = {
            section.id: SectionImages.objects.filter(
                section_id=section).count()
            for section in sections
        }

        images = SectionImages.objects.all().order_by(
            "display_order",
            "alt_text"
            )
        show_images = images.exists()

        videos = SectionVideo.objects.all().order_by(
            "display_order",
            "video_alt_text"
            )
        show_videos = videos.exists()

    except Exception as e:
        error_message = f"A general error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    context = {
        "project": project,
        "categories": categories,
        "show_categories": show_categories,
        "learnings": learnings,
        "show_learnings": show_learnings,
        "sections": sections,
        "show_sections": show_sections,
        "images": images,
        'section_image_counts': section_image_counts,
        "show_images": show_images,
        "videos": videos,
        "show_videos": show_videos
    }

    return render(
        request,
        "projects/project_details.html",
        context,
    )


def client_registration_list(request):
    """
    CRUD basis for the client registration list page
    """
    current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

    if request.user.is_superuser:
        try:
            # Add all new users/clients to the client table
            users = User.objects.all().order_by("username")
            for a_user in users:
                client_allow_delete = not a_user.is_superuser
                if not_in_clients(a_user):
                    new_client = Client(
                        client=a_user,
                        consultant_id=current_consultant,
                        email=a_user.email,
                        allow_delete=client_allow_delete
                    )
                    new_client.save()

            # Get a list of all clients
            registrations = Client.objects.filter(
                consultant=current_consultant).order_by(
                "client", "approval_date"
            )
            show_registrations = registrations.exists()

        except Exception as e:
            error_message = f"A general error occurred: {e}."
            print(error_message)
            print(type(e))
            return redirect('home')

        context = {
            "registrations": registrations,
            "show_registrations": show_registrations
        }

        return render(
            request,
            "projects/client_registration_list.html",
            context,
        )
    else:
        context = {"show_registrations": False}
        return render(
            request,
            "projects/client_registration_list.html",
            context,
        )


def client_delete(request, username):
    """
    Delete an individual client.
    """
    try:
        # only superusers can delete clients
        if request.user.is_superuser:
            user = User.objects.get(username=username)
            user.delete()

    except DatabaseError as e:
        error_message = f"A Database error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    except Exception as e:
        error_message = f"A general error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

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

            # Send email to potential client
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
        error_message = f"A Database error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    except Exception as e:
        error_message = f"A general error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    return HttpResponseRedirect(reverse('client_registration_list'))


def new_project(request):
    """
    Shows new project page
    """
    return render(
        request,
        "projects/new_project.html",
    )
