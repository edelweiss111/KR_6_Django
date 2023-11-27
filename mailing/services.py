from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_mailing(client_list, message):
    try:
        send_mail(
            message.subject,
            message.body,
            EMAIL_HOST_USER,
            client_list
        )
    except Exception:
        raise Exception
