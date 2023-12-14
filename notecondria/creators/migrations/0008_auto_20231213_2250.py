# Generated by Django 3.1.3 on 2023-12-14 04:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0007_auto_20231213_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creator',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='verificationcode',
            name='code',
            field=models.CharField(default='LJtBFx', max_length=255),
        ),
        migrations.AlterField(
            model_name='verificationcode',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 14, 5, 0, 19, 556162, tzinfo=utc)),
        ),
    ]
