import requests
from decouple import config

from django.http import HttpResponseBadRequest


GOOGLE_CAPTCHA_API_URL = 'https://www.google.com/recaptcha/api/siteverify'


def validate_captcha(g_recaptcha_response: str) -> HttpResponseBadRequest:
    if config('APP_ENV') == 'development':
        return None

    res = requests.post(
        GOOGLE_CAPTCHA_API_URL,
        data={
            'secret': config('RECAPTCHA_SECRET'),
            'response': g_recaptcha_response
        }
    )
    body = res.json()
    success = body['success']
    if res.status_code != 200 or not success:
        return HttpResponseBadRequest('캡챠 인증에 실패했습니다')
