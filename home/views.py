from django.shortcuts import render, reverse
from .models import Consultant, Skill, PastEmployment, PressLink, Config, Customer, SocialAccount, How
from projects.models import Project
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.http import HttpResponseRedirect
from projects.utils import client_approved

# Create your views here.

def consultant_home(request):
    """
    Renders the home page
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        consultant = Consultant.objects.filter(consultant_id=current_consultant).first()        
        
        socials = SocialAccount.objects.filter(consultant_id=current_consultant)
        
        customers = Customer.objects.filter(consultant_id=current_consultant)
        show_customers = False if customers.count() == 0 else True

        if request.user.is_authenticated:
            if client_approved(request.user):
                # show all projects
                projects = Project.objects.filter(consultant_id = current_consultant, show_in_home = True).order_by("display_order", "title")  
            else:
                # show only non-confidential projects
                projects = Project.objects.filter(consultant_id = current_consultant, confidential = False, show_in_home = True ).order_by("display_order", "title")
        else:
            # show only non-confidential projects
            projects = Project.objects.filter(consultant_id = current_consultant, confidential = False ).order_by("display_order", "title")

        show_projects = False if projects.count() == 0 else True
        
    except Exception as e:
        error_message = f"A general error occurred:: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
    context = {"consultant": consultant,
                "socials": socials,
                "customers": customers,
                "show_customers": show_customers,
                "projects": projects,
                "show_projects": show_projects
                }
    
    # let's append the config data for CSS custom properties to the context dictionary
    context.update(settings.CONTEXT_CONFIG_DATA)
    
    return render(
        request,
        "home/home.html",
        context,
    )

def consultant_about(request):
    """
    Renders the home page
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        consultant = Consultant.objects.filter(consultant_id=current_consultant).first()
        
        skills = Skill.objects.filter(consultant_id=current_consultant, type=1).order_by("display_order", "label")
        show_skills = False if skills.count() == 0 else True

        tools = Skill.objects.filter(consultant_id=current_consultant, type=2).order_by("display_order", "label")
        show_tools = False if tools.count() == 0 else True
        
        hows = How.objects.filter(consultant_id=current_consultant).order_by("display_order")
        show_how = False if tools.count() == 0 else True

        interests = Skill.objects.filter(consultant_id=current_consultant, type=3).order_by("display_order", "label")
        show_interests = False if interests.count() == 0 else True

        roles = Skill.objects.filter(consultant_id=current_consultant, type=4).order_by("display_order", "label")
        show_roles = False if roles.count() == 0 else True

        pastemployments = PastEmployment.objects.filter(consultant_id=current_consultant)
        show_pastemployments = False if pastemployments.count() == 0 else True

        presslinks = PressLink.objects.filter(consultant_id=current_consultant)
        show_presslinks = False if presslinks.count() == 0 else True
        
    except Exception as e:
        error_message = f"A general error occurred:: {e}. Please try again later."
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)  
    
    context = {"consultant": consultant,
                "skills": skills,
                "show_skills": show_skills,
                "tools": tools,
                "show_tools": show_tools,
                "interests": interests,
                "show_interests": show_interests,
                "roles": roles,
                "show_roles": show_roles,
                "pastemployments": pastemployments,
                "show_pastemployments": show_pastemployments,
                "presslinks": presslinks,
                "show_presslinks": show_presslinks,
                "hows": hows,
                "show_how": show_how
                }
    
    # let's append the config data for CSS custom properties to the context dictionary
    context.update(settings.CONTEXT_CONFIG_DATA)
    
    return render(
        request,
        "home/about.html",
        context,
    )

def reload_config(request):
    try:
        CURRENT_CONSULTANT = Config.objects.get(key="CURRENT_CONSULTANT").value
        # get all config data for the current consultant from the db
        # and update the dictionary
        consultant = Consultant.objects.get(consultant_id=CURRENT_CONSULTANT)
        settings.CONTEXT_CONFIG_DATA['consultant_fname'] = consultant.first_name
        settings.CONTEXT_CONFIG_DATA['consultant_lname'] = consultant.last_name
        settings.CONTEXT_CONFIG_DATA['consultant_email'] = consultant.email
        
        # get all config data for the current consultant from the db
        configs = Config.objects.filter(consultant_id=CURRENT_CONSULTANT)
        # let's load these into a dictionary
        for this_config in configs:
            settings.CONTEXT_CONFIG_DATA[this_config.key] = this_config.value

        return HttpResponseRedirect(reverse('home'))
    
    except Exception as e:
        error_message = f"An error occurred while reloading config: {e}"
        print(error_message)
        print(type(e))
        return HttpResponse(error_message, status=500)