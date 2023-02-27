# Generated by Django 4.0.8 on 2022-11-05 12:19
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0015_alter_question_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "1: One text input"),
                    (2, "2: Two text inputs"),
                    (5, "5: One choice selection"),
                ],
                default=1,
            ),
        ),
    ]
