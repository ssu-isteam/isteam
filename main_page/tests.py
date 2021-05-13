from django.test import TestCase
from .models import Introduction


class MainPageViewTest(TestCase):
    mock_intro: Introduction

    @classmethod
    def setUpTestData(cls):
        cls.mock_intro = Introduction(
            title="test",
            body="test",
            photo="media/helloWorld.png",
            activation=True
        ).save()

    def test_get_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'<div class="main__isteam-intro__features" id="test">')
