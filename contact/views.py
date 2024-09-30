import logging
from django.shortcuts import render
from .models import CollaborationRequest
from .forms import CollaborationForm
from django.core.mail import send_mail
from django.db import DatabaseError
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def collaboration_request_list(request):
    """
    Renders the CR list page
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']
        
        crs = CollaborationRequest.objects.filter(consultant_id = current_consultant).order_by("-request_date", "last_name")      
        show_crs = False if crs.count() == 0 else True
    
    except Exception as e:
        error_message = f"A general error occurred in collaboration request list: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
    context = {"crs": crs,
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
                
                current_cr = CollaborationRequest.objects.filter(open=True).order_by("-request_date").first()
                
                # Send email to potential client
                client_message = (
                    f"Hi {current_cr.first_name},\n\n"
                    "Thanks for your message!\n\n"
                    "The collaboration request for "
                    f"{settings.CONTEXT_CONFIG_DATA['consultant_fname']} {settings.CONTEXT_CONFIG_DATA['consultant_lname']} ({settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']})" 
                    f" was received and {settings.CONTEXT_CONFIG_DATA['consultant_fname']} will respond at the earliest convenience.\n"
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
                    f"Hi {settings.CONTEXT_CONFIG_DATA['consultant_fname']}!\n\n"
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
                    [settings.CONTEXT_CONFIG_DATA['consultant_email']],
                    fail_silently=False,
                )                

            except DatabaseError as e:
               error_message = f"A Database error occurred: {e}. Please try again later."
               print(error_message)
               print(type(e))
               return HttpResponse(error_message, status=500)    
            
            except Exception as e:
               error_message = f"A general error occurred in contact(): {e}. Please try again later."
               print(error_message)
               print(type(e))
               return HttpResponse(error_message, status=500)  
        
        else:
            print(f"A form validation error occurred")
            return render(request, "contact/contact.html", {"collaboration_form": collaboration_form})    

    collaboration_form = CollaborationForm()
    
    context = {        
                "collaboration_form": collaboration_form
                }
    
    return render(
        request,
        "contact/contact.html",
        context,
    )
    
  
