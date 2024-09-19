from django.shortcuts import render, get_object_or_404
from .models import CollaborationRequest

# Create your views here.
def CollaborationRequest_list(request):
    """
    Renders the CR list page
    """
    queryset = CollaborationRequest.objects.filter(open=True).order_by("-request_date")
    crs = get_object_or_404(queryset)

    return render(
        request,
        "contact/collaborationrequest_list.html",
        {"crs": crs,
        
        },
    )