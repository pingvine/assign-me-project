from django.test import TestCase
from person.models import Person
from person.constants import STATUS_EXAMINER


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = Person.objects.create(
            first_name='Jenny-Penny',
            last_name='Johansson',
            status=STATUS_EXAMINER,
            email='benny@penny.com',
            cellphone='+46761234567',
        )

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first_name')

    def test_last_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last_name')

    def test_status_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_email_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_cellphone_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('cellphone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 20)

    def test_last_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 40)

    def test_email_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_cellphone_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('cellphone').max_length
        self.assertEqual(max_length, 15)

    def test_get_absolute_url(self):
        person = Person.objects.get(id=1)
        self.assertEqual(person.get_absolute_url(), '/person/1/')
