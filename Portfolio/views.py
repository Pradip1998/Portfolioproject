from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    abouts = About.objects.all()
    eduations = Education.objects.all().order_by('id')
    experiences = Experience.objects.all().order_by('id')
    categories = SkillCategory.objects.all()
    certifications= Certification.objects.all()
    projects = Project.objects.all()
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



