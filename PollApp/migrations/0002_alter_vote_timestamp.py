# Generated by Django 4.1.7 on 2023-08-24 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 22, 14, 31, 940165, tzinfo=datetime.timezone.utc)),
        ),
    ]
