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
