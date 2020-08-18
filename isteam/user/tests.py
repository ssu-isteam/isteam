import json

from django.test import TestCase, Client

from user.models import Member


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
    def setUpTestData():
        u1 = Member.objects.create(
            username='1234',
            first_name='이',
            last_name='정현',
            student_id='12345678',
            password='1234',
            email_verified=True
        )

        u1.save()

    def test_user_sign_in(self):
        req_body = {
            'nickname': '1234',
            'password': '1234'
        }
        response = self.client.post('/user/signin/', req_body)
        print(response)
        self.assertEqual(response.status_code, 200)