from django import forms 
from .models import Project


class CreateProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'title',
            'image',
            'url_github',
            'url_demo',
            'tags'
            ]