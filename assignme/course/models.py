from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='courses')

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return '{author} : {body}'.format(author=self.author, body=self.body)
