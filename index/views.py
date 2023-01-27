from django.shortcuts import render

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from projects.models import Project

class Index(View):

    def get(self, request):

        projects = Project.objects.all()

        context = {
            'projects': projects
        }

        return render(request, 'index.html', context)



