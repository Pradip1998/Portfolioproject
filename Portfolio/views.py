from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import os


# Create your views here.

def home(request):
    abouts = About.objects.all()
    eduations = Education.objects.all().order_by('id')
    experiences = Experience.objects.all().order_by('id')
    categories = SkillCategory.objects.all()
    certifications= Certification.objects.all()
    projects = Project.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        information = request.POST['information']
        someth = Message(name=name, email=email, subject=subject, information=information)
        someth.save()
        send_mail(name,
                  'Thankyou for your message',
                  'pradipchapagain123@gmail.com',
                  [email])
    return render(request, 'index.html', {'abouts': abouts,'eduations':eduations,'experiences' : experiences,'categories': categories,'certifications': certifications,'projects' :projects})


def education(request,id):
    eduations = Education.objects.get(pk=id)
    return render(request, 'education.html', {'eduations': eduations})

def project(request, id):
    project = Project.objects.get(pk=id)
    return render(request, 'projects.html', {'project': project})

def index(request):
    abouts = About.objects.all()
    eduations = Education.objects.all().order_by('id')
    experiences = Experience.objects.all().order_by('id')
    categories = SkillCategory.objects.all()
    certifications = Certification.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html',
                  {'abouts': abouts, 'eduations': eduations, 'experiences': experiences, 'categories': categories,
                   'certifications': certifications, 'projects': projects})


def certificate(request, id ):
    certificate = Certification.objects.get(pk=id)
    return render(request, 'certificate.html', {'certificate': certificate})


def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'pics', 'work.png')  # Provide the correct path to your file
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        return HttpResponse("File not found", status=404)



def footer_data(request):
    abouts = About.objects.all()
    return render(request,'test.html',{ 'abouts': abouts})






