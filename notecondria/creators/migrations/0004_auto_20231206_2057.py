# Generated by Django 3.1.3 on 2023-12-07 02:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0003_auto_20231205_2312'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivationCode',
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='code',
            field=models.CharField(default='koBMEe', max_length=255),
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 3, 7, 26, 890083, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='function',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='max_use',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='usage',
            field=models.CharField(choices=[('R', 'Register'), ('A', 'Authenticate'), ('F', 'Function')], default='A', max_length=1),
        ),
    ]
