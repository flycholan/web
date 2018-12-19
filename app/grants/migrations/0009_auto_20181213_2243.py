# Generated by Django 2.1.2 on 2018-12-13 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0008_merge_20181210_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='last_contribution_date',
            field=models.DateTimeField(default=datetime.datetime(1990, 1, 1, 0, 0), help_text='The last contribution date'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='next_contribution_date',
            field=models.DateTimeField(default=datetime.datetime(1990, 1, 1, 0, 0), help_text='The next contribution date'),
        ),
    ]
