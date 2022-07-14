from django.contrib import admin

from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'value_proposition']


admin.site.register(Project, ProjectAdmin)