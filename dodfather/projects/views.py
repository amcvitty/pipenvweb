from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages


from .models import Project, Measure
from .forms import ProjectForm, NewProjectMeasuresFormSet, EditProjectMeasuresFormSet


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    model = Project
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Project.objects.filter(title__icontains=query).order_by('-created_at')


class ProjectCreateView(generic.CreateView):
    form_class = ProjectForm
    template_name = 'projects/new.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['measures_form'] = NewProjectMeasuresFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        measures_form = NewProjectMeasuresFormSet(self.request.POST)
        if form.is_valid() and measures_form.is_valid():
            return self.form_valid(form, measures_form)
        else:
            return self.form_invalid(form, measures_form)

    def form_valid(self, form, measures_form):
        self.object = form.save(commit=False)
        self.object.save()
        # saving Measure Instances by attaching the project
        measures = measures_form.save(commit=False)
        for measure in measures:
            measure.project = self.object
            measure.save()
        return HttpResponseRedirect(reverse("projects:index"))

    def form_invalid(self, form, measures_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  measures_form=measures_form
                                  )
        )


def delete(request, pk):
    if request.method != 'POST':
        raise Http404("Must use POST on delete")
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, f'Deleted project {project}')
    return HttpResponseRedirect(reverse('projects:index'))


def edit(request, pk):
    # if this is a POST request we need to process the form data
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, instance=project)
        measures_form = EditProjectMeasuresFormSet(
            request.POST, instance=project)

        # check whether it's valid:
        if form.is_valid() and measures_form.is_valid():
            project = form.save()
            measures_form.save()
            messages.success(request, f'Saved project {project}')
            return HttpResponseRedirect(reverse('projects:detail', args=(project.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm(instance=project)
        measures_form = EditProjectMeasuresFormSet(instance=project)

    return render(request, 'projects/edit.html', {'form': form, 'measures_form': measures_form})


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    # Add measures into the context
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['measures'] = Measure.objects.filter(
            project=context['project'])
        return context
