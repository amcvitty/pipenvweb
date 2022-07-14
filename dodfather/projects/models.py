from django.db import models
from django.forms import ModelForm
import datetime
from django.utils import timezone


# class User(models.Model)
# class Measure(models )

class Project(models.Model):

    DOODLING = 'D'
    IN_PROGRESS = 'I'
    ABANDONED = 'A'
    COMPLETED = 'C'
    RESPECIFYING = 'R'

    STATUS_CHOICES = [
        (DOODLING, 'Doodling'),
        (IN_PROGRESS, 'In Progress'),
        (ABANDONED, 'Abandoned'),
        (COMPLETED, 'Completed'),
        (RESPECIFYING, 'Respect'),
    ]
    title = models.CharField(max_length=5)
    value_proposition = models.TextField(max_length=2000)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default=DOODLING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.created_at = timezone.now()

    def __str__(self):
        return self.title

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'value_proposition', 'status']
