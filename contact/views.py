from django.shortcuts import render, redirect
from .models import CollaborationRequest
from .forms import CollaborationForm
from django.core.mail import send_mail
from django.db import DatabaseError
from django.conf import settings


def collaboration_request_list(request):
    """
    Renders the Collaboration Request (CR) list page
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        crs = CollaborationRequest.objects.filter(
            consultant_id=current_consultant
        ).order_by("-request_date", "last_name")

        show_crs = crs.exists()

    except Exception as e:
        error_message = f"A general error occurred in cr list: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    context = {
        "crs": crs,
        "show_crs": show_crs
    }

    return render(
        request,
        "contact/collaboration_request_list.html",
        context,
    )


def contact(request):
    """Handle collaboration requests."""
    if request.method == "POST":
        collaboration_form = CollaborationForm(data=request.POST)
        if collaboration_form.is_valid():
            try:
                collaboration_form.save()

                current_cr = CollaborationRequest.objects.filter(
                    open=True).order_by(
                    "-request_date"
                ).first()

                # Send email to potential client
                client_message = (
                    f"Hi {current_cr.first_name},\n\n"
                    "Thanks for your message!\n\n"
                    "The collaboration request for "
                    f"{settings.CONTEXT_CONFIG_DATA['consultant_fname']} "
                    f"{settings.CONTEXT_CONFIG_DATA['consultant_lname']} "
                    f"({settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']}) "
                    f"was received and "
                    f"{settings.CONTEXT_CONFIG_DATA['consultant_fname']} "
                    "will respond at the earliest convenience.\n"
                    "\nKind regards"
                )

                send_mail(
                    "[NO-REPLY] Collaboration Request received",
                    client_message,
                    "",
                    [current_cr.email],
                    fail_silently=False,
                )

                # Send email to consultant
                consultant_message = (
                    f"Hi "
                    f"{settings.CONTEXT_CONFIG_DATA['consultant_fname']}!\n\n"
                    "YEAH!! You have a new collaboration request:\n\n"
                    "----------------------\n"
                    f"Name (last, first): {current_cr.last_name}, "
                    f"{current_cr.first_name}\n"
                    "----------------------\n"
                    f"Email: {current_cr.email}\n"
                    "----------------------\n"
                    f"Message:\n{current_cr.message}\n"
                    "----------------------\n"
                    f"Request date: {current_cr.request_date}\n"
                    "----------------------\n"
                    "\nYour friendly Portfolio App django"
                )

                send_mail(
                    "[NO-REPLY] You have a Collaboration Request",
                    consultant_message,
                    "",
                    [settings.CONTEXT_CONFIG_DATA['consultant_email']],
                    fail_silently=False,
                )

            except DatabaseError as e:
                error_message = (
                    f"A Database error occurred in contact(): {e}. "
                    "Please try again later."
                )
                print(error_message)
                print(type(e))
                return redirect('home')

            except Exception as e:
                error_message = f"A general error occurred in contact(): {e}"
                print(error_message)
                print(type(e))
                return redirect('home')

        else:
            print("A form validation error occurred")
            return render(
                request,
                "contact/contact.html",
                {"collaboration_form": collaboration_form}
            )

    collaboration_form = CollaborationForm()

    context = {
        "collaboration_form": collaboration_form
    }

    return render(
        request,
        "contact/contact.html",
        context,
    )


def custom_404_view(request, exception):
    """
    Custom view to handle 404 errors and redirect to the home page.
    """
    return redirect('home')
