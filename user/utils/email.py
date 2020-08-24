from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def build_template_email(title, template_name, to, context=None) -> EmailMessage:
    body = render_to_string(template_name, context=context)
    return EmailMessage(title, body, to=[to])