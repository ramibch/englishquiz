# Generated by Django 4.2.4 on 2023-12-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0019_question_linkedin_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='linkedin_poll_commented',
            field=models.BooleanField(default=False),
        ),
    ]
