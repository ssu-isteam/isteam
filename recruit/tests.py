from django.test import TestCase
from django.urls import reverse
from django.contrib.admin import ACTION_CHECKBOX_NAME

from typing import List

from .models import Recruitment
from groupware.models import Semester
from user.models import Member


class ProfileFormViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get('/recruit/submit/')
        self.assertEqual(response.status_code, 200)


class QuestionFormViewTest(TestCase):
    def test_redirected_if_cookie_not_exists(self):
        response = self.client.get('/recruit/questions/submit')
        self.assertEqual(response.status_code, 302)


class RecruitmentMakePublishedTest(TestCase):
    mock_admin: Member
    mock_recruitments: List[Recruitment]

    @classmethod
    def create_mock_recruitments(cls) -> List[Recruitment]:
        mock_recruitments: List[Recruitment] = []

        for i in range(5):
            mock_recruitments.append(
                Recruitment(
                    is_published=True,
                    information=f'info-{i}',
                    semester=Semester.FIRST,
                    year=2021
                )
            )

        mock_recruitments[0].is_published = False

        Recruitment.objects.bulk_create(mock_recruitments)
        return Recruitment.objects.all()

    @classmethod
    def create_mock_admin(cls) -> Member:
        return Member.objects.create_superuser(
            username='admin',
            email='foo@bar.com',
            password='foobar'
        )

    @classmethod
    def setUpTestData(cls):
        cls.mock_recruitments = cls.create_mock_recruitments()
        cls.admin = cls.create_mock_admin()

    def test_success(self):
        target = self.mock_recruitments[0]

        url = reverse('admin:recruit_recruitment_changelist')
        request_body = {
                'action': 'make_published',
                ACTION_CHECKBOX_NAME: [target.pk]
            }
        self.client.force_login(self.admin)
        response = self.client.post(url, request_body)

        found = Recruitment.objects.get(pk=target.pk)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(found.is_published)
        self.assertTrue(all(r.is_published is not True for r in self.mock_recruitments[1:]))
