from django.shortcuts import render

from .models import Project, Tecnologias

def home(request):
    projects = Project.objects.all()
    tecnologias = Tecnologias.objects.all()
    
    return render(request, 'home.html', {'projects' : projects, 'tecnologias' : tecnologias})
