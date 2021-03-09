from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from handins.models import Handin, Assignment


class HandinIndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK')

        test_user1.save()

        number_of_handins = 13
        assignment = Assignment(title='TDDD11',
                                description='A desc.',
                                deadline=datetime.today())
        assignment.save()

        for handin_id in range(number_of_handins):
            Handin.objects.create(
                holder=f'Student {handin_id}',
                attached_files=f'url {handin_id}',
                assignment=assignment)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/handins/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('handins_index'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('handins_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'handins_index.html')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('handins_index'))

        self.assertRedirects(response, '/accounts/login/?next=/handins/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('handins_index'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'handins_index.html')
