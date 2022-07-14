from django.test import TestCase

import datetime

from django.utils import timezone
from django.urls import reverse

from .models import Project


class ProjectModelTests(TestCase):
    def test_can_be_created(self):
        project = Project(title="Chef migration",
                          value_proposition="Getting money for nothing")

        self.assertIs(project.title, "Chef migration")

    def test_can_be_saved(self):
        project = Project(title="Chef migration",
                          value_proposition="Getting money for nothing")
        project.save()
        self.assertIs(project.title, "Chef migration")
        project.refresh_from_db()
        self.assertIsNot(project.created_at, None)


# Tests fetching via MVC
# class QuestionDetailViewTests(TestCase):
#     def test_future_question(self):
#         """
#         The detail view of a question with a pub_date in the future
#         returns a 404 not found.
#         """
#         future_question = create_question(
#             question_text='Future question.', days=5)
#         url = reverse('polls:detail', args=(future_question.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)

#     def test_past_question(self):
#         """
#         The detail view of a question with a pub_date in the past
#         displays the question's text.
#         """
#         past_question = create_question(
#             question_text='Past Question.', days=-5)
#         url = reverse('polls:detail', args=(past_question.id,))
#         response = self.client.get(url)
#         self.assertContains(response, past_question.question_text)
