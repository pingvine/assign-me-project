import os
from django.db import models
from datetime import datetime


def get_upload_path(instance, filename):
    return os.path.join(instance.assignment.title,
                        instance.holder,
                        datetime.now().strftime("%H-%M-%S"),
                        instance.filename(),
                        )


class Handin(models.Model):
    holder = models.CharField(max_length=100)
    attached_files = models.FileField(upload_to=get_upload_path)
    created_on = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)

    def filename(self):
        return os.path.basename(self.attached_files.name)

    def __str__(self):
        return '{} - {}'.format(self.holder, self.created_on)


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
