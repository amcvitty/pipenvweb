from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages

import logging

from .models import Project, ProjectForm


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


def new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_project = form.save()
            messages.success(request, f'Added project {new_project}')
            return HttpResponseRedirect(reverse('projects:detail', args=(new_project .id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()

    return render(request, 'projects/new.html', {'form': form})


def edit(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if request.POST['delete_project']:
            project = get_object_or_404(Project, pk=pk)
            project.delete()
            messages.success(request, f'Deleted project {project}')
            return HttpResponseRedirect(reverse('projects:index'))

        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            project = form.save()
            messages.success(request, f'Added project {project}')
            return HttpResponseRedirect(reverse('projects:detail', args=(project.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        project = get_object_or_404(Project, pk=pk)
        form = ProjectForm(instance=project)

    return render(request, 'projects/edit.html', {'form': form})


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def delete(self, request):
        return render(request, 'projects/delete.html', {project: self.get_object()})
    # def get_queryset(self):
    #     return Project.objects.filter(
    #         pub_date__lte=timezone.now())
