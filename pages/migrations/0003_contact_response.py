# Generated by Django 4.1 on 2022-08-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='response',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
