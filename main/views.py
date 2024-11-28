from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Tag

def portfolio_view(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'], form_data['phone'])
        send_mail('You got a mail!', message, '', ['dianaveaudry@gmail.com'])  # TODO: enter your email address

    return render(request, 'contact.html', {})


def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "projects.html", {"project": project})

def redirect_view(request):
    response = redirect('/home')
    return response