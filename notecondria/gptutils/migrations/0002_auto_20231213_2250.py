# Generated by Django 3.1.3 on 2023-12-14 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gptutils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conversation',
            name='last_use',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
