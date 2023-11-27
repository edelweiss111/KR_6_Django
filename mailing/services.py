from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_mailing(client_list, message):
    try:
        for client in client_list:
            send_mail(
                message.subject,
                message.body,
                EMAIL_HOST_USER,
                [client]
            )
    except Exception:
        raise Exception
