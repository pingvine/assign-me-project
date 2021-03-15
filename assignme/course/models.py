from django.db import models
from django.urls import reverse
from person.constants import STATUS_EXAMINER


class Category(models.Model):
    name = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='courses')

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.code

    def get_examiner(self):
        for member in self.staff.all():
            if member.status == STATUS_EXAMINER:
                return member


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    is_reply = models.BooleanField(default=False)
    reply = models.ForeignKey(
        'Comment', on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return '{author} : {body}'.format(author=self.author, body=self.body)
