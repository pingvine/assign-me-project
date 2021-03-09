from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from person.models import Person
from person.constants import STATUS_EXAMINER


class PersonIndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK')

        test_user1.save()

        number_of_persons = 13

        for person_id in range(number_of_persons):
            Person.objects.create(
                first_name=f'Name {person_id}',
                last_name=f'Lastname {person_id}',
                status=STATUS_EXAMINER)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/person/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('person_index'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('person_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'person_index.html')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('person_index'))

        self.assertRedirects(response, '/accounts/login/?next=/person/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('person_index'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person_index.html')
