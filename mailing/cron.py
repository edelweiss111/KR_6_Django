import smtplib
from datetime import datetime, timedelta
from calendar import monthrange
from mailing.models import Mailing, Log
from mailing.services import send_mailing


def start_mailing():
    now = datetime.now()
    mailing_list = Mailing.objects.filter(date__lte=now, time__lte=now)
    created_mailing_list = [mailing for mailing in mailing_list if mailing.status == 'created']

    for mailing in created_mailing_list:
        mailing.status = 'started'
        mailing.save()

        clients = mailing.client.all()
        message = mailing.message
        try:
            send_mailing(clients, message)

            Log.objects.create(time=now, status=True, server_response='', mailing=mailing)
            mailing.status = 'created'
            if mailing.periodisity == 'day':
                mailing.date += timedelta(days=1)
            elif mailing.periodisity == 'week':
                mailing.date += timedelta(weeks=1)
            elif mailing.periodisity == 'month':
                month = now.month
                year = now.year
                days_count = monthrange(year, month)
                mailing.date += timedelta(days=days_count[1])
        except smtplib.SMTPException as e:
            Log.objects.create(time=now, status=False, server_response=e, mailing=mailing)
            mailing.status = 'created'
        finally:
            mailing.save()
