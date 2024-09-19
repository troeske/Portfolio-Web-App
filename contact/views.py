from django.shortcuts import render
from .models import CollaborationRequest
from .forms import CollaborationForm
from datetime import datetime

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
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if request.method == "POST":
        collaboration_form = CollaborationForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.request_date = datetime.datetime.now()
            collaboration_form.save()

    collaboration_form = CollaborationForm()
    
    return render(
        request,
        "contact/contact.html",
        {        
        "collaboration_form": collaboration_form
        },
    )
