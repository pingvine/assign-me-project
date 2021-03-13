from django.test import TestCase
from course.models import Course, Comment


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(
            title='TDDX21', body='Ave maria its ti me to shower')

    def test_title_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_body_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_title_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_title(self):
        course = Course.objects.get(id=1)
        expected_object_name = course.code
        self.assertEqual(expected_object_name, str(course))

    def test_get_absolute_url(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.get_absolute_url(), '/course/1/')


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        course = Course(title='TDDD12', body='Big boody')
        course.save()

        Comment.objects.create(
            author='TDDX21', body='Ave maria its ti me to shower', course=course)

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_body_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_title_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('author').max_length
        self.assertEqual(max_length, 60)

    def test_object_name_is_auhtor(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = '{author} : {body}'.format(
            author=comment.author, body=comment.body)
        self.assertEqual(expected_object_name, str(comment))
