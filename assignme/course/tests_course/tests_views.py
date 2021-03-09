from django.test import TestCase
from django.urls import reverse

from course.models import Course


class CourseIndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_courses = 13

        for course_id in range(number_of_courses):
            Course.objects.create(
                title=f'Kurs {course_id}',
                body=f'Beskrivning {course_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('course_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('course_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'course_index.html')
