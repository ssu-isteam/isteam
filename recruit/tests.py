from django.test import TestCase


class ProfileFormViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get('/recruit/submit/')
        self.assertEqual(response.status_code, 200)


class QuestionFormViewTest(TestCase):
    def test_redirected_if_cookie_not_exists(self):
        response = self.client.get('/recruit/questions/submit')
        self.assertEqual(response.status_code, 302)
