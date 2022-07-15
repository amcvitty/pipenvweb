from django.db import models
import datetime
from django.utils import timezone
# class User(models.Model)


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
    title = models.CharField(max_length=50)
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


class Measure(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
