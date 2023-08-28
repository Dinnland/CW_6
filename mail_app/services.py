import logging
from datetime import timedelta

import schedule
from django.core.mail import send_mail
from django.utils import timezone

from CW6 import settings
from mail_app.models import *


def sending_mail(subject, body, clients_email):
    """Отправление письма"""
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        clients_email
    )


def send_mailing():
    """Рассылка. запуск отправки писем в зависимости от текущего времени"""
    mailing_settings = MailingSettings.objects.all()
    current_time = timezone.now()
    frequency = {'daily': 1, 'weekly': 7, 'monthly': 30}
    for mailing in mailing_settings:
        # Начало рассылки
        if mailing.mailing_status == 'created' or mailing.mailing_status == 'started':
            print(1)
            if mailing.mailing_start_time <= current_time <= mailing.mailing_end_time:
                print(2)
                for client in mailing.clients.all():
                    letter_subject = mailing.mail.letter_subject
                    letter_body = mailing.mail.letter_body
                    print(3)
                    try:
                        print(4)
                        print(settings.EMAIL_HOST_USER, settings.EMAIL_USE_SSL)
                        send_mail(letter_subject, letter_body, settings.EMAIL_HOST_USER, [client.email])
                        # Создание лога рассылки при успехе
                        MailingLogs.objects.create(
                            mailing=mailing,
                            client=client,
                            attempt_status='successful',
                            server_response='Сообщение успешно отправлено',
                        )
                        mailing.mailing_status = 'started'
                        mailing.mailing_start_time += timedelta(days=frequency.get(mailing.mailing_period))
                        mailing.save()

                    except Exception as error:
                        # Создание лога рассылки при ошибке
                        MailingLogs.objects.create(
                            mailing=mailing,
                            client=client,
                            attempt_status='failed',
                            server_response=str(error),
                        )
            # Конец рассылки
            elif mailing.mailing_end_time <= current_time:
                print(5)
                mailing.mailing_status = 'completed'
                mailing.save()
            else:
                pass


def job():
    schedule.every(5).seconds.do(send_mailing)
    logging.info('Новая задача добавлена')

