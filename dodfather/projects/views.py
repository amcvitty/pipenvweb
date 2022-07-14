from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Project, ProjectForm


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    model = Project


def new(request):
    model = Project
    template_name = 'projects/detail.html'

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


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    # def get_queryset(self):
    #     return Project.objects.filter(
    #         pub_date__lte=timezone.now())
