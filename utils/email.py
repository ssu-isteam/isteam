from django.core.mail import send_mail
from django.template import loader


def send_template_email(title, template_name, to, context=None):
    template = loader.get_template(template_name)
    body = template.render(context)
    return send_mail(title, body, '', [to], html_message=body)
