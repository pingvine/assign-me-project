import os
from datetime import datetime
from django.db import models
from .constants import FILE_TYPES, FILE_TYPE_DEFAULT


def get_upload_path(instance, filename):
    return os.path.join(instance.assignment.title.replace(' ', '-'),
                        instance.holder,
                        datetime.now().strftime("%H-%M-%S"),
                        instance.filename(),
                        )


def get_formating_type_from_name(filename):
    ending = filename.split('.')[-1]
    for ending_pair in FILE_TYPES:
        if ending in ending_pair[0]:
            return ending
    return FILE_TYPE_DEFAULT


class Handin(models.Model):
    holder = models.CharField(max_length=100)
    attached_files = models.FileField(upload_to=get_upload_path)
    created_on = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)

    objects = models.Manager()

    def filename(self):
        return os.path.basename(self.attached_files.name)

    def __str__(self):
        return '{} - {}'.format(self.holder, self.created_on)

    def get_format_type(self):
        return get_formating_type_from_name(self.attached_files.name)


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

    objects = models.Manager()

    def __str__(self):
        return self.title
