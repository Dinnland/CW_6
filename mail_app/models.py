from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """Клиент сервиса:"""
    email = models.EmailField(max_length=254, verbose_name='email')
    name = models.CharField(max_length=100, verbose_name='name')
    surname = models.CharField(max_length=100, verbose_name='surname')
    patronymic = models.CharField(max_length=100, verbose_name='patronymic', **NULLABLE)
    comment = models.CharField(max_length=300, verbose_name='comment', **NULLABLE)

    def __int__(self):
        return f'{self.email} {self.name} {self.surname}'

    def __str__(self):
        return f'{self.email} {self.name} {self.surname}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('email',)

#
# class Mailing(models.Model):
#     """НИХУЯ НЕ ПОНИМАЮ  С ЭТИМИ ПЕРИОДИЧНОСТЯМИ, РАЗБЕРИИИИСССССССССССССЬ"""
#     # mailing_time = models.TimeField( verbose_name='mailing_time')
#     # mailing_periodicity = models.CharField(max_length=100, verbose_name='mailing_periodicity')
#     # mailing_status = models.CharField(max_length=100, verbose_name='mailing_status')
#
#     def __int__(self):
#         return f'{self.mailing_time} {self.mailing_periodicity} {self.mailing_status}'
#
#     def __str__(self):
#         return f'{self.mailing_time} {self.mailing_periodicity} {self.mailing_status}'
#
#     class Meta:
#         verbose_name = 'Mailing'
#         verbose_name_plural = 'Mailings'
#         ordering = ('mailing_time',)


class MessageToMailing(models.Model):
    """Сообщение для рассылки"""
    letter_subject = models.CharField(max_length=500, verbose_name='letter_subject')
    letter_body = models.TextField(verbose_name='letter_body')

    def __int__(self):
        return f'{self.letter_subject} {self.letter_body} '

    def __str__(self):
        return f'{self.letter_subject} {self.letter_body}'

    class Meta:
        verbose_name = 'MessageToMailing'
        # verbose_name_plural = 'Mailings'
        ordering = ('letter_subject',)


class MailingLogs(models.Model):
    """Логи рассылки"""
    datetime_of_last_attempt = models.DateTimeField(verbose_name='datetime_of_last_attempt')
    attempt_status = models.BooleanField(verbose_name='attempt_status')
    mail_server_response = models.CharField(max_length=600, verbose_name='mail_server_response')

    def __int__(self):
        return f'{self.datetime_of_last_attempt} {self.attempt_status} '

    def __str__(self):
        return f'{self.datetime_of_last_attempt} {self.attempt_status}'

    class Meta:
        verbose_name = 'MailingLogs'
        # verbose_name_plural = 'Mailings'
        ordering = ('attempt_status',)

