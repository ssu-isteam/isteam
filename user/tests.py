import json

from django.test import TestCase, RequestFactory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AnonymousUser

from user.models import Member
from user.views.sign_in import SignIn


class SignUpViewTest(TestCase):
    def test_sign_up_and_send_email(self):
        req_body = {
            'nickname': 'asdf',
            'name': '이정현',
            'student_id': '12345678',
            'email': 'jeonghyun0126@outlook.com',
            'password': '1234',
            're_password': '1234'
        }
        response = self.client.post('/user/signup/', data=req_body)
        self.assertNotEqual(response.status_code, 500)


class SignInViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.member = Member.objects.create_user(
            username='1234',
            first_name='이',
            last_name='정현',
            student_id='12345678',
            password='1234',
            is_active=True,
            did_sign_up=True
        )

    def test_user_sign_in_success(self):
        req_body = {
            'nickname': '1234',
            'password': '1234'
        }

        response = self.client.post('/user/signin/', data=req_body, follow=True)
        self.assertNotEqual(response.status_code, 401)

    def test_user_sign_in_fail(self):
        req_body = {
            'nickname': '1234',
            'password': '1235'
        }

        response = self.client.post('/user/signin/', data=req_body, follow=True)
        self.assertEqual(response.status_code, 401)
