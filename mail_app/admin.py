from django.contrib import admin
from mail_app.models import Client, MessageToMailing, MailingLogs, MailingSettings


# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Клиенты"""
    list_display = ('email', 'name', 'surname', 'patronymic', 'comment')
    list_filter = ('email',)
    search_fields = ('name', 'email', 'surname',)


@admin.register(MessageToMailing)
class MessageToMailingAdmin(admin.ModelAdmin):
    """Сообщение для рассылки"""
    list_display = ('letter_subject', 'letter_body')
    list_filter = ('letter_subject',)
    search_fields = ('letter_subject',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    """Рассылка"""
    list_display = ('title', 'mailing_start_time', 'mailing_end_time', 'mailing_period', 'mailing_status' )
    # list_display = ('__all__',)

    list_filter = ('mailing_start_time', 'mailing_end_time', 'mailing_period', 'clients',)
    search_fields = ('title', 'clients')
    ordering = ('-mailing_status',)


@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    """Логи рассылки"""
    list_display = ('timestamp', 'attempt_status', 'server_response', 'client', 'mailing')
    list_filter = ('attempt_status', 'server_response', 'client',)
    search_fields = ('timestamp', 'client', 'mailing',)
    ordering = ('-timestamp',) #сортировка по последнему времени попытки

