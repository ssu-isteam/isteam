import requests
from decouple import config

def get_captcha_data(recaptcha_response):
    return requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': config('RECAPTCHA_SECRET'),
        'response': recaptcha_response
    })
