# Generated by Django 5.1.1 on 2024-10-02 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_cd_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='mediareservations',
            name='date_due',
            field=models.DateField(default=datetime.date(2024, 10, 9)),
        ),
    ]