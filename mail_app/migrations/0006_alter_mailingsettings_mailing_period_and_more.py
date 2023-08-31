# Generated by Django 4.2.3 on 2023-08-30 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_app', '0005_alter_mailingsettings_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='mailing_period',
            field=models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=50, verbose_name='Периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='mailing_status',
            field=models.CharField(choices=[('completed', 'Завершена'), ('created', 'Создана'), ('started', 'Запущена'), ('off', 'Отключена')], default='created', max_length=50, verbose_name='Статус рассылки'),
        ),
    ]