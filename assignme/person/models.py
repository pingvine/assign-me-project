import os
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
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
    courses = models.ManyToManyField(
        Course, related_name="staff", blank=True)

    website = models.CharField(
        'website url', max_length=100, blank=True)
    github = models.CharField(
        'github username', max_length=50, blank=True)
    twitter = models.CharField(
        'twitter username', max_length=50, blank=True)
    instagram = models.CharField(
        'instagram username', max_length=50, blank=True)
    facebook = models.CharField(
        'facebook url', max_length=100, blank=True)

    objects = models.Manager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"pk": self.pk})

    def get_website_label(self):
        return self.website.split('.', 1)[1]

    def get_github_url(self):
        github_url_start = 'https://github.com/'
        return github_url_start + self.github

    def get_twitter_url(self):
        github_url_start = 'https://twitter.com/'
        return github_url_start + self.twitter

    def get_instagram_url(self):
        github_url_start = 'https://www.instagram.com/'
        return github_url_start + self.instagram
