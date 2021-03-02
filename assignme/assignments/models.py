from django.db import models


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    image = models.FilePathField(path="/img")

    def __str__(self):
        return self.title
