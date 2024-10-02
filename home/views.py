from django.shortcuts import render, reverse, redirect
from .models import (
    Consultant, Skill, PastEmployment, PressLink, Config,
    Customer, SocialAccount, How
)
from projects.models import Project
from django.conf import settings
from django.http import HttpResponseRedirect
from projects.utils import client_approved


def consultant_home(request):
    """
    Renders the home page for the consultant.

    This view function retrieves the current consultant's information, social
    accounts, customers, and projects to display on the home page. It handles
    different scenarios based on the user's authentication status and whether
    the user is approved as a client.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page with the consultant's information,
        social accounts, customers, and projects.

    Context:
        consultant (Consultant): The current consultant object.
        socials (QuerySet): A queryset of the consultant's social accounts.
        customers (QuerySet): A queryset of the consultant's customers.
        show_customers (bool): A flag indicating whether to show customers.
        projects (QuerySet): A queryset of the consultant's projects.
        show_projects (bool): A flag indicating whether to show projects.

    Exceptions:
        Redirects to the home page if an exception occurs and logs the error
        message.
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        consultant = Consultant.objects.filter(
            consultant_id=current_consultant
        ).first()

        socials = SocialAccount.objects.filter(
                consultant_id=current_consultant)

        customers = Customer.objects.filter(consultant_id=current_consultant)
        show_customers = customers.exists()

        if request.user.is_authenticated:
            if client_approved(request.user):
                # show all projects
                projects = Project.objects.filter(
                    consultant_id=current_consultant, show_in_home=True
                ).order_by("display_order", "title")
            else:
                # show only non-confidential projects
                projects = Project.objects.filter(
                    consultant_id=current_consultant, confidential=False,
                    show_in_home=True
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
        "consultant": consultant,
        "socials": socials,
        "customers": customers,
        "show_customers": show_customers,
        "projects": projects,
        "show_projects": show_projects,
    }

    return render(request, "home/home.html", context)


def consultant_about(request):
    """
    Renders the about page for the current consultant.

    This view function retrieves various details about the current consultant,
    including their skills, tools, interests, roles, past employments, press
    links, and methodologies (hows). It then renders the 'about' page with
    this information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'about' page with the consultant's details.

    Context:
        consultant (Consultant): The current consultant object.
        skills (QuerySet): A queryset of the consultant's skills.
        show_skills (bool): Whether the consultant has any skills.
        tools (QuerySet): A queryset of the consultant's tools.
        show_tools (bool): Whether the consultant has any tools.
        interests (QuerySet): A queryset of the consultant's interests.
        show_interests (bool): Whether the consultant has any interests.
        roles (QuerySet): A queryset of the consultant's roles.
        show_roles (bool): Whether the consultant has any roles.
        pastemployments (QuerySet): A queryset of past employments.
        show_pastemployments (bool): Are there any past employments.
        presslinks (QuerySet): A queryset of the consultant's press links.
        show_presslinks (bool): Whether the consultant has any press links.
        hows (QuerySet): A queryset of the consultant's methodologies (hows).
        show_how (bool): Whether the consultant has any methodologies.

    Raises:
        Exception: If any error occurs during the retrieval of consultant
                   details, an error message is printed and the user is
                   redirected to the home page.
    """
    try:
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']

        consultant = Consultant.objects.filter(
            consultant_id=current_consultant
        ).first()

        skills = Skill.objects.filter(
            consultant_id=current_consultant, type=1
        ).order_by("display_order", "label")
        show_skills = skills.exists()

        tools = Skill.objects.filter(
            consultant_id=current_consultant, type=2
        ).order_by("display_order", "label")
        show_tools = tools.exists()

        hows = How.objects.filter(
            consultant_id=current_consultant
        ).order_by("display_order")
        show_how = hows.exists()

        interests = Skill.objects.filter(
            consultant_id=current_consultant, type=3
        ).order_by("display_order", "label")
        show_interests = interests.exists()

        roles = Skill.objects.filter(
            consultant_id=current_consultant, type=4
        ).order_by("display_order", "label")
        show_roles = roles.exists()

        pastemployments = PastEmployment.objects.filter(
            consultant_id=current_consultant
        )
        show_pastemployments = pastemployments.exists()

        presslinks = PressLink.objects.filter(
            consultant_id=current_consultant
        )
        show_presslinks = presslinks.exists()

    except Exception as e:
        error_message = f"A general error occurred: {e}."
        print(error_message)
        print(type(e))
        return redirect('home')

    context = {
        "consultant": consultant,
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
        "show_how": show_how,
    }

    return render(request, "home/about.html", context)


def reload_config(request):
    """
    Reloads the configuration settings for the current consultant from the
    database and updates the global context configuration data.

    This function performs the following steps:
    1. Retrieves the current consultant's ID from the configuration.
    2. Fetches the consultant's details (first name, last name, email)
       and updates the global context configuration data.
    3. Fetches all configuration settings for the current consultant
       and updates the global context configuration data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the 'home' view on success.
        HttpResponse: Redirects to the 'home' view on error, with an
                      error message printed to the console.
    """
    try:
        CURRENT_CONSULTANT = Config.objects.get(key="CURRENT_CONSULTANT").value
        # get all config data for the current consultant from the db
        # and update the dictionary
        consultant = Consultant.objects.get(consultant_id=CURRENT_CONSULTANT)
        settings.CONTEXT_CONFIG_DATA['consultant_fname'] = \
            consultant.first_name
        settings.CONTEXT_CONFIG_DATA['consultant_lname'] = consultant.last_name
        settings.CONTEXT_CONFIG_DATA['consultant_email'] = consultant.email

        # get all config data for the current consultant from the db
        configs = Config.objects.filter(consultant_id=CURRENT_CONSULTANT)
        # load these into a dictionary
        for this_config in configs:
            settings.CONTEXT_CONFIG_DATA[this_config.key] = this_config.value

        return HttpResponseRedirect(reverse('home'))

    except Exception as e:
        error_message = f"An error occurred while reloading config: {e}"
        print(error_message)
        print(type(e))
        return redirect('home')
