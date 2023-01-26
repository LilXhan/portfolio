from django.urls import path 
from . import views

urlpatterns = [
    path('projects', views.AllProject.as_view(), name='projects'),
    path('project/create', views.CreateProjectView.as_view(), name='create'),
    path('project/delete/<int:id>', views.delete_project, name='delete')
]