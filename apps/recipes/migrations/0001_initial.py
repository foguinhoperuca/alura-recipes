# Generated by Django 4.1.4 on 2022-12-08 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('preparation', models.TextField()),
                ('preparation_time', models.IntegerField()),
                ('serving', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('date_recipe', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
