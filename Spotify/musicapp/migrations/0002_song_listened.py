# Generated by Django 4.0.1 on 2022-01-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
