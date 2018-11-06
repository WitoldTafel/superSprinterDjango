from django.contrib import admin

# Register your models here.
from Sprinter.models import Project, Story

admin.site.register(Project)
admin.site.register(Story)

