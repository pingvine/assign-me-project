import os
from django.contrib.auth.models import User
from django.db import models
from course.models import Course
from .constants import PERSON_STATUSES


class Person(models.Model):

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'
        ordering = ['first_name', 'last_name']

    first_name = models.CharField('first_name', max_length=20)
    last_name = models.CharField('last_name', max_length=40)
    status = models.CharField(choices=PERSON_STATUSES, max_length=50)

    email = models.EmailField('email', blank=True)
    cellphone = models.CharField('phone', max_length=15, blank=True)
    image = models.ImageField('picture',
                              upload_to='img/profiles',
                              blank=True,
                              null=True)

    user = models.OneToOneField(
        User,
        blank=True,
        null=True,
        verbose_name='user',
        on_delete=models.CASCADE,
    )
    courses = models.ManyToManyField(Course, related_name="staff", blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
