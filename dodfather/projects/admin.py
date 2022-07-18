from django.contrib import admin

from .models import Project, Measure
# Register your models here.


class MeasureInline(admin.TabularInline):
    model = Measure


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'value_proposition', 'status']
    inlines = [MeasureInline, ]


admin.site.register(Project, ProjectAdmin)
