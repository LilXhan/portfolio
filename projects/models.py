from django.db import models

from taggit.managers import TaggableManager

class Project(models.Model):

    image = models.CharField(max_length=400)
    title = models.CharField(max_length=20)
    url_github = models.CharField(max_length=400)
    url_demo = models.CharField(max_length=400)
    tags = TaggableManager()

    class Meta:
        db_table = 'projects'