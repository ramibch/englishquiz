# Generated by Django 4.0.5 on 2022-07-19 20:47
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("socialmedia", "0010_alter_tweet_twitter_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstagramPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instagram_id", models.CharField(max_length=50)),
                ("text", models.TextField(max_length=1000)),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "api_delete",
                    models.BooleanField(
                        default=False,
                        help_text="It gets deleted after clicking on Save",
                        verbose_name="Delete from Instagram",
                    ),
                ),
                (
                    "api_deleted",
                    models.BooleanField(
                        default=False, verbose_name="Already deleted from Instagram"
                    ),
                ),
            ],
        ),
    ]
