from django.shortcuts import render, redirect

from django.views.generic import ListView, View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import CreateProject
from .models import Project

# Create your views here.

def delete_project(request, id):
    
    p = Project.objects.get(pk=id)
    p.delete()

    return redirect('projects')

class AllProject(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects.html'


class CreateProjectView(LoginRequiredMixin, View):


    def get(self, request):

        form = CreateProject()

        context = {
            'form': form 
        }

        return render(request, 'create.html', context)

    
    def post(self, request):
        form = CreateProject(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user 
            obj.save()
        
            form.save_m2m()
            return redirect('projects')



