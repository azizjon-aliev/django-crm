# Generated by Django 5.1.5 on 2025-01-28 08:25

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='contract_number',
            field=models.CharField(blank=True, help_text='Введите номер лицевого счета или договора', max_length=50, null=True, verbose_name='Лицевой счет/договор'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='phone_number',
            field=models.CharField(help_text='Введите номер телефона клиента', max_length=20, validators=[django.core.validators.RegexValidator(message='Номер телефона должен начинаться с +992 и содержать 9 цифр после кода страны.', regex='^\\+992\\d{9}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='service_phone_number',
            field=models.CharField(blank=True, help_text='Введите номер телефона, связанный с услугой', max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен начинаться с +992 и содержать 9 цифр после кода страны.', regex='^\\+992\\d{9}$')], verbose_name='Номер телефона услуги'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='subject',
            field=models.CharField(choices=[], help_text='Выберите тему обращения', max_length=200, verbose_name='Тема обращения'),
        ),
        migrations.AddIndex(
            model_name='customerrequest',
            index=models.Index(fields=['first_name'], name='CustomerSup_first_n_4cf824_idx'),
        ),
        migrations.AddIndex(
            model_name='customerrequest',
            index=models.Index(fields=['last_name'], name='CustomerSup_last_na_df764e_idx'),
        ),
        migrations.AddIndex(
            model_name='customerrequest',
            index=models.Index(fields=['email'], name='CustomerSup_email_dcc2d1_idx'),
        ),
        migrations.AddIndex(
            model_name='customerrequest',
            index=models.Index(fields=['phone_number'], name='CustomerSup_phone_n_7704b7_idx'),
        ),
        migrations.AddIndex(
            model_name='customerrequest',
            index=models.Index(fields=['subject'], name='CustomerSup_subject_015402_idx'),
        ),
        migrations.AddIndex(
            model_name='customerrequest',
            index=models.Index(fields=['contract_number'], name='CustomerSup_contrac_c2f07a_idx'),
        ),
    ]
