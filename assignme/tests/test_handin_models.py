from datetime import datetime
from django.test import TestCase
from handins.models import Handin, Assignment
from course.models import Course


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        course = Course(title='TDDD12', body='Big boody')
        course.save()

        assignment = Assignment(
            title='TDDD11', description='Very big yes', deadline=datetime.today(), course=course)
        assignment.save()

        handin = Handin.objects.create(
            holder='TDDX21', attached_files='ada/beda/ceda', assignment=assignment)
        handin.save()

    def test_holder_label(self):
        handin = Handin.objects.get(id=1)
        field_label = handin._meta.get_field('holder').verbose_name
        self.assertEqual(field_label, 'holder')

    def test_attached_files_label(self):
        handin = Handin.objects.get(id=1)
        field_label = handin._meta.get_field('attached_files').verbose_name
        self.assertEqual(field_label, 'attached files')

    def test_holder_max_length(self):
        handin = Handin.objects.get(id=1)
        max_length = handin._meta.get_field('holder').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title(self):
        handin = Handin.objects.get(id=1)
        expected_object_name = f'{handin.holder} - {handin.created_on}'
        self.assertEqual(expected_object_name, str(handin))

    def test_get_absolute_url(self):
        handin = Handin.objects.get(id=1)
        self.assertEqual(handin.get_absolute_url(), '/handins/1/')


class AssignmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        course = Course(title='TDDD12', body='Big boody')
        course.save()

        assignment = Assignment(
            title='TDDD11', description='Very big yes', deadline=datetime.today(), course=course)
        assignment.save()

    def test_title_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_title_max_length(self):
        assignment = Assignment.objects.get(id=1)
        max_length = assignment._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title(self):
        assignment = Assignment.objects.get(id=1)
        expected_object_name = assignment.title
        self.assertEqual(expected_object_name, str(assignment))
