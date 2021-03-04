from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory

from typing import List, Tuple
import json
import random

from .models import Recruitment, Answer, Question, Applicant
from groupware.models import Semester
from user.models import Member
from recruit.views.question_form import QuestionFormView


def create_mock_recruitments(howmany: int) -> List[Recruitment]:
    mock_recruitments: List[Recruitment] = []

    for i in range(howmany):
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


def create_mock_questions(howmany: int, recruitment: Recruitment) -> List[Question]:
    mock_questions: List[Question] = []

    for i in range(howmany):
        mock_questions.append(
            Question(
                question=f'test-question-{i}',
                recruitment=recruitment
            )
        )

    Question.objects.bulk_create(mock_questions)
    return Question.objects.all()


class ProfileFormViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get('/recruit/submit/')
        self.assertEqual(response.status_code, 200)


class QuestionFormViewTest(TestCase):
    def test_redirected_if_cookie_not_exists(self):
        response = self.client.get('/recruit/questions/submit')
        self.assertEqual(response.status_code, 302)


class ProfileAndQuestionIntegrationTest(TestCase):
    mock_recruitments: List[Recruitment]

    mock_questions: List[Question]

    mock_cookie: Tuple[str, str]

    @classmethod
    def setUpTestData(cls):
        cls.mock_recruitments = create_mock_recruitments(1)
        cls.mock_recruitments[0].is_published = True
        cls.mock_recruitments[0].save()

        cls.mock_questions = create_mock_questions(1, cls.mock_recruitments[0])

        cookie_user1 = json.dumps({
            'username': 'aaa',
            'student_id': '12341234',
            'email': 'jeonghyun0126@outlook.com',
            'phone_number': '01012341234'
        })
        cookie_user2 = json.dumps({
            'username': 'bbb',
            'student_id': '43214321',
            'email': '_dream@kakao.com',
            'phone_number': '01012344321'
        })
        cls.mock_cookie = cookie_user1, cookie_user2

    @staticmethod
    def create_get_request_factory(cookie: str):
        rf = RequestFactory().get(reverse('recruit_question'))
        rf.COOKIES['profile'] = cookie
        return rf

    def create_post_request_factory(self, cookie: str) -> Tuple[RequestFactory, map]:
        body = {
            'g-recaptcha-response': 'foo',
            self.mock_questions[0].pk: str(random.random())
        }

        rf = RequestFactory().post(
            path=reverse('recruit_question'),
            data=body,
        )
        rf.COOKIES['profile'] = cookie

        return rf, body

    def test_question_form_reads_cookie_data_from_independent_session(self):
        cookie_user1, cookie_user2 = self.mock_cookie

        question_form_view = QuestionFormView.as_view()

        question_form_view(self.create_get_request_factory(cookie_user1))
        question_form_view(self.create_get_request_factory(cookie_user2))

        prf_user1, body_user1 = self.create_post_request_factory(cookie_user1)
        prf_user2, body_user2 = self.create_post_request_factory(cookie_user2)

        response_user1 = question_form_view(prf_user1)
        response_user2 = question_form_view(prf_user2)

        self.assertEqual(response_user1.status_code, 302)
        self.assertEqual(response_user2.status_code, 302)

        persisted_answers = Answer.objects.all().count()
        self.assertEqual(persisted_answers, 2)

        persisted_answer_1 = Answer.objects.get(applicant__name='aaa')
        persisted_answer_2 = Answer.objects.get(applicant__name='bbb')

        self.assertEqual(body_user1[self.mock_questions[0].pk], persisted_answer_1.answer)
        self.assertEqual(body_user2[self.mock_questions[0].pk], persisted_answer_2.answer)

    @classmethod
    def tearDownClass(cls) -> None:
        Answer.objects.all().delete()
        Recruitment.objects.all().delete()


class RecruitmentMakePublishedTest(TestCase):
    mock_admin: Member
    mock_recruitments: List[Recruitment]

    @classmethod
    def create_mock_admin(cls) -> Member:
        return Member.objects.create_superuser(
            username='admin',
            email='foo@bar.com',
            password='foobar'
        )

    @classmethod
    def setUpTestData(cls):
        cls.mock_recruitments = create_mock_recruitments(5)
        cls.admin = cls.create_mock_admin()

    def test_success(self):
        target = self.mock_recruitments[0]

        url = reverse('admin:recruit_recruitment_changelist')
        request_body = {
                'action': 'make_published',
                '_selected_action': [target.pk]
            }
        self.client.force_login(self.admin)
        response = self.client.post(url, request_body)

        found = Recruitment.objects.get(pk=target.pk)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(found.is_published)
        self.assertTrue(all(r.is_published is not True for r in self.mock_recruitments[1:]))
