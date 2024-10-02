# THE LIVING RESUME
This is a web site / app to showcase the portfolio and resume of developers, UX/UI designers or even consultants in general: [MY LIVING RESUME](https://portfolio-site-consultant-ee5192104007.herokuapp.com/) . 
<br>
<img src="xxx"  width="300" height="auto" alt="Portfolio home">

I was inspired to implement this web app to help developers (e.g. me), UX/UI designers and consultants (herein referred to as 'consultants') showcase their ever evolving experience in an easy to maintainable way. Current resume sites are static and adding or changing content on the site, in most cases, requires editing the html code of the site. As it is the nature of what we do, every day, we will expand our skills and gain experience and our public available portfolio should reflect that. This puts the need for easy editing and extending on the forefront of the LIVING RESUME web app.

In addition it is also in the nature of what we do, that some projects we work on are confidential. Thus the LIVING RESUME provides for a controlled log-in to be able to showcase confidential projects after registration and approval.

The LIVING RESUME web app can be deployed for one consultant. However the structure is prepared to host any number of consultants in it's database. Each consultant can customize the appearance (colors, text sizes, fonts). For each consultant a dedicated heroku deployment will be setup ensuring that proprietary domains can be used. All deployments will access the same model (stored in a single postgreSQL).

I will use this web app to implement my resume and portfolio of projects.

## Requirements/Personas and EPICS
The LIVING RESUME will provide an appealing overview of a developer's or UI/UX designer's capabilities and portfolio for potential clients interested to hire this consultant on a full-time, part-time or per project basis. The site thus has to cater for the following two main user <b>personas</b>:

    (1) the client looking to evaluate the developer/UI-/UX designer 's skills, experience, past projects and capabilities in order to make a decision to potentially hire
    (2) the consultant who wants to showcase their skills, experience, past projects and capabilities through information on the site.

In order to best showcase their experience and portfolio, consultants have the following needs:

1. separation of the content into:
    1. **Home**: Summary and teaser info.
    2. **About**: All information about the consulting including:
        - Intro (personal info, roles, core expertise and focus, way of working, and why hire)
        - Last 4 past employers with position and time
        - List of skills either rated with a number value to represent proficiency level or by a textual description
        - List of interests
        - List of tools used
        - Links to press articles
    3. **Reference Projects**: A list of all public projects the consultant participated in with images representing each project and a short summary of the project. Each entry in the list can be clicked and leads to a detailed project page. An account/login feature will allow a client to sign-up and once approved by the consultant to login and then also see confidential projects.
    4. **Project Details**: Each project is a concatenation of sections. Each section has:
        - Up to two headings
        - One or more pictures or videos
        - A text block
        - Optionally a link to an external resource
        - The consultant can add as many sections to a project as necessary. Projects thus can have a varying number of sections.

2. give potential clients an easy way to get in contact with the consultant:
    4. **Collaborate Request**: a client will be able to initiate a collaboration request through a contact form on the site providing email, name, request description and should receive an email confirmation of the request.

3. allow the consultant to maintain any content/info of the site without needing to re-program HTML/CSS. Ideally this function is a part of the site itself. However as a first step using django interface is sufficient to:
    1. **Manage Information**: change all presented information about the consultant incl. photos, roles, description etc. 
    2. **Manage Experience, Skills etc.**: add new or change existing skills, tools used, roles, customers, past employments
    3. **Manage projects and their details**: add new or change existing project references incl. descriptions, sections, images/videos etc.
    4. **Manage projects confidentiality**: set/change a project to ‘confidential’ / ‘public’.
    5. **Manage Client Sign-ups**: view, approve and delete sign-up requests of potential clients. 
    6. **View Collaboration Requests**: view all received collaboration requests.


## User Experience

### Target Audience:

1. **Companies/employers** (aka clients): who searching for developers (e.g. me), UX/UI designers and consultants to hire or engage them for a project.
2. **Developers, UX/UI designers or consultants** (aka consultants -> me): who want to showcase their experience, skill and portfolio of projects in an easy to maintain way


### User Stories:
The epics above are broken down in to user stories here: [Github User Stories](https://github.com/users/troeske/projects/7/views/2?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D/)


### Future Use-Cases

    (1) Content management within the site
    (2) advance customization options   

## Design
### Site Structure
The LIVING RESUME web app is structured into the following apps:

1. **Home**. This shows the general information of the consultant incl. work history, roles, interests etc. split into two main views: Home and About
2. **Projects**. This provides an overview of all projects in the portfolio incl. details and the option to create a new project. It also hosts the approval logic for new client sign-up requests. It includes the following main views: project_list, project_details, registrations, new_project.
3. **Contact**. Submit a collaboration request. It's main views are: contact and collaboration_request_list
4. **Sign-up**. Client/user sign-up (allauth).


### Wireframes
__Mobile First approach:__

<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898562/wf_home_mobile_kbkb9e.png"  width="300" height="auto" alt="home page mobile">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898558/wf_about_mobile_npwq7s.png"  width="300" height="auto" alt="about page mobile">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898558/wf_project_list_mobile_vqun7g.png"  width="300" height="auto" alt="projects list mobile page">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898558/wf_project_1_mobile_vi21hw.png"  width="300" height="auto" alt="project details mobile page">

<br>

__Tablet and Desktop:__

<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898558/wf_home_desktop_a6g15y.png"  width="300" height="auto" alt="home page desktop">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898559/wf_about_desktop_lkaoyc.png"  width="300" height="auto" alt="about page desktop">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898558/wf_project_list_desktop_iys4fy.png"  width="300" height="auto" alt="projects list desktop page">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898558/wf_project_1_desktop_xdr9sr.png"  width="300" height="auto" alt="project details desktop page">



## Database Entity Relationship Diagram ##

[ERD (Lucidchart)](https://lucid.app/lucidchart/a84194fd-bb5b-4516-8860-a5ce5b77cad4/edit?beaconFlowId=5B48F8E11F7B68FE&invitationId=inv_49416297-33a5-4be2-9a57-03776dd9937d&page=0_0#)

<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884243/ERD_projects_thyfjo.png"  width="1000" height="auto" alt="home page desktop">
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884244/ERD_consultants_pvxvq3.png"  width="1000" height="auto" alt="home page desktop">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884243/ERD_clients_cuqwti.png"  width="500" height="auto" alt="home page desktop">
<br>

### Imagery used
Simple iconography for intuitive and clean UI.

### Color Scheme
configurable: currently shades of gray
        
### Typography
For the showcase, al normal text is based on the sans-serif free Google font Inter while headings are based on the free font Rychardwalker

## Current Features:

### Styling through database config
To enable a consultant to change the basic appearance of the LIVING RESUME without changing the css, the LIVING RESUME implements a database approach to managing a first selection of styling options. In future releases more options will be made available. 

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727902490/screenshot_admin_interface_config_model_qkadec.png"  width="300" height="auto" alt="collaboration request">
<br>

To achieve this database storage of styling parameters, the site is using css custom properties. When a page is loaded the config model is read and respective values are stored in css custom properties. The only way I found was to use django template language for html files and injected the respective part of css code into the html page through a [style] section.

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727903033/screenshot_db_config_css_cust_prop_in_html_yyremo.png"  width="300" height="auto" alt="collaboration request">
<br>

### Home
### About
### Project List
### Project Details

The first viewport of the detail project page
<br>

### Add project
Consultants will constantly add to their project portfolio. To have a first option to add such a new project to their LIVING RESUME, the consultant (superuser/admin) can use the [Site Admin] menu to 'add project'. The add project page will guide the consultant through the process using links to the django admin interface.

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727902030/screenshot_new_project_qr6re2.png"  width="300" height="auto" alt="collaboration request">
<br>

### Contact

The contact / collaboration form allows a potential client to get in contact with the consultant.
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898982/screenshot_contact_fdviz3.png"  width="300" height="auto" alt="collaboration request">
<br>

If the user is alreader signe-up the contact form is prefilled with any existing data known about the user:
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727901537/screenshot_contact_signed_in_plpvzc.png"  width="300" height="auto" alt="collaboration request">
<br>

### Sign-up/Sign-in/Sign-out

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898983/screenshot_sign-up_wpjlr8.png"  width="300" height="auto" alt="sign-up">

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898983/screenshot_sign-in_wr7kyc.png"  width="300" height="auto" alt="sign in">

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898984/screenshot_sign-out_qaefoc.png"  width="300" height="auto" alt="sign-out">

### Status of  the current login state

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727899191/screenshot_user_auth_status_jvpuc5.png"  width="300" height="auto" alt="sign-out">

### Access to confidential projects after login

Clients can only see projects that are marked as confidential if they have signed-in and have been approved by the consultant (superuser/admin) e.g. after signing an NDA or providng additional data.

### Approval of signed-up clients

The consultant (superuser/admin) can approve individual clients who have signed-up via the [site admin] menue of the LIVING RESUME site after signing-in

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727898654/screenshot_1_registrations.html_hpgrwm.png"  width="300" height="auto" alt="registration approval">

### Overview of all collaboration requests

<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884242/screenshot_collaborationrequests_igrj5v.png"  width="300" height="auto" alt="collaboration requests">

### Full CRUD
__C__ reate: The [Contact Form](https://portfolio-site-consultant-ee5192104007.herokuapp.com/contact/) implements the create part through a form POST view
<br>
__R__ ead: almost every page implements a read from the database as all displayed info is stored in the respective model. E.g. (when logged in a superuser/admin) [registrations list](https://portfolio-site-consultant-ee5192104007.herokuapp.com/projects/client_registration_list)
<br>
__U__ pdate: the (when logged in a superuser/admin) [registration list](https://portfolio-site-consultant-ee5192104007.herokuapp.com/projects/client_registration_list) implements an update of the field [approved] in the Client model (projects app) setting approved=True through the approve_client(request, id) view.
<br>
__D__ delete: the (when logged in a superuser/admin) [registration list](https://portfolio-site-consultant-ee5192104007.herokuapp.com/projects/client_registration_list) also implements the delete function through the [Delete] button and client_delete(request, username) view.
<br>

## Manual/End-to-End Testing

__Various Browsers on mobile and desktop devices:__
| Test Case ID                                           | Description                                                                                                                                                                                    | Expected Result                                                                                        | Comments                                                                                                    | android- chrome | android- firefox | android- edge | iOS - Safari | iOS-Chrome | desktop- Safari | desktop- chrome | desktop- firefox |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | --------------- | ---------------- | ------------- | ------------ | ---------- | --------------- | --------------- | ---------------- |
| 1\. Home Page                                          |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 1.1                                                    | Verify that the home page loads successfully.                                                                                                                                                  | Home page loads without errors.                                                                        |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.2                                                    | Verify that the home page NavBar displays the correct Brand (consultant name)                                                                                                                  | Title is displayed correctly.                                                                          |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.3                                                    | Verify that the navigation menu links are present and functional.                                                                                                                              | All links are functional.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.4                                                    | Verify that only the featured projects marked 'show_iny_home' are displayed correctly and that confidential project are not shown when user is not logged in and has beedn approved            | Featured projects are displayed.                                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.5                                                    | Verify that the footer contains the user authentication status correct information.                                                                                                            | Footer information is correct.                                                                         |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.6                                                    | Verify that the home page is responsive                                                                                                                                                        | Home page is responsive.                                                                               |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.7                                                    | Verify that the home page is accessible (e.g., screen reader compatibility).                                                                                                                   | Home page is accessible.                                                                               |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2\. About Page                                         |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 2.1                                                    | Verify that the about page loads successfully.                                                                                                                                                 | About page loads without errors.                                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.2                                                    | Verify that the home page NavBar displays the correct Brand (consultant name)                                                                                                                  | Brand is displayed correctly.                                                                          |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.3                                                    | Verify that the consultants information is displayed correctly.                                                                                                                                | Consultants information is correct.                                                                    |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.4                                                    | Verify that the navigation menu links are present and functional.                                                                                                                              | All links are functional.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.5                                                    | Verify that the about page is responsive.                                                                                                                                                      | About page is responsive.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.6                                                    | Verify that the about page is accessible (e.g., screen reader compatibility).                                                                                                                  | About page is accessible.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3\. Contact/CollaborationForm Page                     |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 3.1                                                    | Verify that the contact page loads successfully.                                                                                                                                               | Contact page loads without errors.                                                                     |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.2                                                    | Verify that the collaborationrequest form is present and functional.                                                                                                                           | Contact form is functional.                                                                            |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.3                                                    | Verify that the user can submit the form with valid details.                                                                                                                                   | Form submission is successful.                                                                         |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.4                                                    | Verify that the user and the consultant receive confirmation messages via email after submitting the form.                                                                                     | Confirmation message is displayed.                                                                     |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.5                                                    | Verify that the form displays error messages for invalid inputs.                                                                                                                               | Error messages are displayed.                                                                          |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.6                                                    | Verify that the contact page is responsive and displays correctly on different devices.                                                                                                        | Contact page is responsive.                                                                            |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.7                                                    | Verify that the contact page is accessible (e.g., screen reader compatibility).                                                                                                                | Contact page is accessible.                                                                            |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4\. Project Details Page                               |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 4.1                                                    | Verify that the project details page loads successfully.                                                                                                                                       | Project details page loads without errors.                                                             |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.2                                                    | Verify that the project title, description, and images are displayed correctly.                                                                                                                | Project details are correct.                                                                           | the scroll-arrows on the image-carousel on non-chrome browsers sometimes need a refresh of the page to show | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.3                                                    | Verify that the navigation menu links are present and functional.                                                                                                                              | All links are functional.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.4                                                    | Verify that all sections are displayed correctly.                                                                                                                                              | Related projects are displayed.                                                                        |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.5                                                    | Verify that the project details page is responsive and displays correctly on different devices.                                                                                                | Project details page is responsive.                                                                    |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.6                                                    | Verify that the project details page is accessible (e.g., screen reader compatibility).                                                                                                        | Project details page is accessible.                                                                    |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5\. Login Page                                         |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 5.1                                                    | Verify that the login page loads successfully.                                                                                                                                                 | Login page loads without errors.                                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.2                                                    | Verify that the user can log in with valid credentials.                                                                                                                                        | Login is successful.                                                                                   |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.3                                                    | Verify that the user receives an error message for invalid credentials.                                                                                                                        | Error message is displayed.                                                                            |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 5.4                                                    | Verify that the user is redirected to the home page after successful login.                                                                                                                    | User is redirected to the dashboard.                                                                   |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.5                                                    | Verify that the page NavBar displays the correct Brand (consultant name)                                                                                                                       |                                                                                                        |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.6                                                    | Verify that the login page is responsive and displays correctly on different devices.                                                                                                          | Login page is responsive.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6\. Registration/Sign-Up Page                          |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 6.1                                                    | Verify that the registration page loads successfully.                                                                                                                                          | Registration page loads without errors.                                                                |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.2                                                    | Verify that the user can register with valid details.                                                                                                                                          | Registration is successful.                                                                            |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.3                                                    | Verify that the user receives an error message for invalid inputs.                                                                                                                             | Error message is displayed.                                                                            |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.4                                                    | Verify that the user is redirected to the home page after successful registration.                                                                                                             | User is redirected to the login page.                                                                  |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.5                                                    | Verify that the page NavBar displays the correct Brand (consultant name)                                                                                                                       |                                                                                                        |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.6                                                    | Verify that the registration page is responsive and displays correctly on different devices.                                                                                                   | Registration page is responsive.                                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.7                                                    | Verify that the registration page is accessible (e.g., screen reader compatibility).                                                                                                           | Registration page is accessible.                                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7\. Projects List Page                                 |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 7.1                                                    | Verify that the projects list page loads successfully.                                                                                                                                         | Projects list page loads without errors.                                                               |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.2                                                    | Verify that all projects are listed correctly not showing confidential project when user is not logged in and has beedn approved                                                               | All projects are listed.                                                                               |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.3                                                    | Verify that each project link navigates to the correct project details page.                                                                                                                   | Links navigate correctly.                                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.4                                                    | Verify that the projects list page is responsive and displays correctly on different devices.                                                                                                  | Projects list page is responsive.                                                                      |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.5                                                    | Verify that the projects list page is accessible (e.g., screen reader compatibility).                                                                                                          | Projects list page is accessible.                                                                      |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8\. Add Project Page (through link to Admin Interface) |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 8.1                                                    | Verify that the add project page loads successfully.                                                                                                                                           | Add project page loads without errors.                                                                 |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.2                                                    | Verify that a user can add a new project with valid details incl. sections, images etc.                                                                                                        | Project is added successfully.                                                                         |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.3                                                    | Verify that the form displays error messages for invalid inputs.                                                                                                                               | Error messages are displayed.                                                                          |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9\. Edit Project Page (Admin Interface)                |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 9.1                                                    | Verify that the edit project page loads successfully.                                                                                                                                          | Edit project page loads without errors.                                                                |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.2                                                    | Verify that a user can edit an existing project with valid details.                                                                                                                            | Project is edited successfully.                                                                        |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.3                                                    | Verify that the form displays error messages for invalid inputs.                                                                                                                               | Error messages are displayed.                                                                          |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10\. Delete Project Page (Admin Interface)             |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 10.1                                                   | Verify that the delete admin interface loads successfully for superuser and is blocked by normal user                                                                                          | Delete project page loads without errors.                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.2                                                   | Verify that a superuser can delete a project.                                                                                                                                                  | Project is deleted successfully.                                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.3                                                   | Verify that all related entries for sections, sectionimages etc. are also deleted                                                                                                              | All dependencies are deleted                                                                           |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.4                                                   | Verify that the deleted project is no longer listed on the projects list page.                                                                                                                 | Deleted project is not listed.                                                                         |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.5                                                   | Verify that the delete project page is responsive and displays correctly on different devices.                                                                                                 | Delete project page is responsive.                                                                     |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 11\. Registrations-List                                |                                                                                                                                                                                                |                                                                                                        |                                                                                                             |                 |                  |               |              |            |                 |                 |                  |
| 11.1                                                   | Verify that the link is displayed for a superuser and loads successfully.                                                                                                                      | Delete project page loads without errors.                                                              |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 11.2                                                   | Verify that all clients that have not been approved yet have a button that allows approval                                                                                                     | list shows approve button for not approved users                                                       |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 11.3                                                   | Verify that all clients except those with admin privilidges have a delete button                                                                                                               | list shows no delete button for admins                                                                 |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 11.4                                                   | Verify that when clicking the approve button the respective client<br>1\. receives an email that he/she is approved<br>2\. is approved and can view confidential projects after logging in<br> | email to the client is send and when confidential project are displayed upon next login                |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 11.5                                                   | Verify that when clicking the delete button a confirmation request is displayed and upon confirmation the respective client<br>is deleted<br>                                                  | client is deleted both from the client model as well as a user and is not shown in the list any longer |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 11.6                                                   | Verify that the delete project page is responsive and displays correctly on different devices.                                                                                                 | Delete project page is responsive.                                                                     |                                                                                                             | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok<br><br>       |


### Open/Known Issues

    (1) on some browsers (e.g. firefox) the scroll arrows for the image carousel in project details are not showing up until a refresh of the page
    (2) 
    

## Code Validation
### CI Python Lint PEP8 Validator https://pep8ci.herokuapp.com/
__Results:__
All python files were checked by the CI Python Linter and no errors remain.
<br>

### W3 HTML Validator https://validator.w3.org/nu/#textarea
__Results:__
All html pages were checked by the w3 html validator, and no errors remain.
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884251/html_checker_home.html_nafjpo.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884251/html_checker_about.html_y3xtwz.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884248/html_checker_project_list.html_tdvq2x.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884247/html_checker_project_details.html_nmrmvz.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884247/html_checker_contact.html_rgv2i3.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884247/html_checker_registration_list.html_jjbz5c.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884247/html_checker_sign-in.html_e5usan.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884247/html_checker_collaboration_list.html_lyjjqz.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884246/html_checker_signup.html_ncayze.png"  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884246/html_checker_new_project.html_eubtx8.png"  width="300" height="auto" alt="W3 HTML Validator Results">

### CSS Validator https://jigsaw.w3.org/css-validator/validator
__Results:__
All CSS files were checked by the w3c CSS validator and no errors remain. Remaining warnings are due to the use of CSS variables.
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884246/w3c_css_style.css_yhtkeu.png"  width="300" height="auto" alt="W3 CSS Validator Results">
<br>

### jshint Validator https://jshint.com/
__Results:__
The js file project_details was checked by the jshint validator, and no errors remain.
<br>
<img src="https://res.cloudinary.com/dqd3t6mmb/image/upload/v1727884243/jshint_project_details.js_rmndiy.png"  width="300" height="auto" alt="jshint Validator Results">
<br>

## Deployment
The app is deployed via Heroku.

Deployment method: Github, Repository: troeske/Portfolio-Web-App 

To LIVING RESUME needs the following _Config Var_:

- CLOUDINARY_URL. link to the cloudinary storage for all media files.
- CURRENT_CONSULTANT. the consultant_id of the consultant this deployment showcases.
- DATABASE_URL. Link to the external postgreSQL database for all other content.
- SECRET_KEY. Project secret key.
- SMTP_PASSWORD- password for the email account used to send email confirmations to clients and consultants


The live link can be found here: [THE LIVING RESUME](https://portfolio-site-consultant-ee5192104007.herokuapp.com/) 

## Credits
### Tutorials
no tutorials were used.

### Code
W3Schools: https://www.w3schools.com/
MDN Web Docs: https://developer.mozilla.org/en-US/
GeeksForGeeks: https://www.geeksforgeeks.org/
Bootstrap: https://getbootstrap.com/docs/5.3/getting-started/introduction/
django: https://www.djangoproject.com/start/overview/


The functions that are based on Github Copilot or ChatGPT are market in the code. 
The basis for most of the inline function/class documentation was provided by Github Copilot.
   
### Graphics
icons: https://fontawesome.com/
favicon: https://www.freepik.com/icon

### Photos

### Any other resources
https://validator.w3.org/nu/#textarea
https://jigsaw.w3.org/css-validator/validator

I used https://tabletomarkdown.com/convert-spreadsheet-to-markdown/ to convert my Google Sheets manual testing matrix into a to table for this readme.


