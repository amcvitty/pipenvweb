from django.forms import ModelForm
from django.forms import inlineformset_factory

from .models import Project, Measure


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'value_proposition', ]


NewProjectMeasuresFormSet = inlineformset_factory(
    Project, Measure, fields=('title', 'description'), extra=3, can_delete=False)
EditProjectMeasuresFormSet = inlineformset_factory(
    Project, Measure, fields=('title', 'description'), extra=3, can_delete=True)
