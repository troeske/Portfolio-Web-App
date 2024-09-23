import logging
from django.shortcuts import render
from .models import CollaborationRequest
from .forms import CollaborationForm
from django.core.mail import send_mail
from portfolio.utils import get_consultant
from django.db import DatabaseError
from django.core.exceptions import ValidationError
from django.http import HttpResponse

# Create your views here.
def collaboration_request_list(request):
    """
    Renders the CR list page
    """
    crs = CollaborationRequest.objects.filter(open=True).order_by("-request_date")

    return render(
        request,
        "contact/collaboration_request_list.html",
        {"crs": crs,
        
        },
    )

def contact(request):
    """Handle collaboration requests."""
    if request.method == "POST":
        collaboration_form = CollaborationForm(data=request.POST)
        if collaboration_form.is_valid():
            try:
                collaboration_form.save()
                
                current_cr = CollaborationRequest.objects.filter(open=True).order_by("-request_date").first()
                consultant_id, consultant_first_name, consultant_last_name, consultant_email = get_consultant(False)
                
                # Send email to potential client
                client_message = (
                    f"Hi {current_cr.first_name},\n\n"
                    "Thanks for your message!\n\n"
                    "The collaboration request for "
                    f"{consultant_first_name} {consultant_last_name} ({consultant_id})" 
                    f" was received and {consultant_first_name} will respond at the earliest convenience.\n"
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
                    f"Hi {consultant_first_name}!\n\n"
                    "YEAH!! You have a new collaboration request:\n\n"
                    "----------------------\n"
                    f"Name (last, first): {current_cr.last_name}, {current_cr.first_name}\n" 
                    "----------------------\n"
                    f"eMail: {current_cr.email}\n"
                    "----------------------\n"
                    f"Message:\n{current_cr.message}\n"
                    "----------------------\n"
                    f"Request date: {current_cr.request_date}\n"
                    "----------------------\n"
                    "\nYour friendly Portfolio App django"
                )
                
                send_mail(
                    "[NO-REPLY] you have a Collaboration Request",
                    consultant_message,
                    "",
                    [consultant_email],
                    fail_silently=False,
                )                

            except DatabaseError as e:
               print(f"A Database error occurred: {e}")
               print(type(e))
               return HttpResponse("A database error occurred. Please try again later.", status=500)    
            
            except Exception as e:
               print(f"A general error occurred: {e}")
               print(type(e))
               return HttpResponse("An unexpected error occurred. Please try again later.", status=500)    

        
        else:
            print(f"A form validation error occurred")
            return render(request, "contact/contact.html", {"collaboration_form": collaboration_form})    

    collaboration_form = CollaborationForm()
    
    return render(
        request,
        "contact/contact.html",
        {        
        "collaboration_form": collaboration_form
        },
    )
    
  
