from django.db import models

ASSIGNMENT_TYPES = [
    ('O0', 'O0'),
    ('O1', 'O1'),
    ('O2', 'O2'),
]


class Handin(models.Model):
    holder = models.CharField(max_length=100)
    attached_files = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    assignment_type = models.CharField(
        max_length=3,
        choices=ASSIGNMENT_TYPES,
        default=None,
    )

    def __str__(self):
        return '{} - {}'.format(self.assignment_type, self.holder)


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
