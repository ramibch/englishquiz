# Generated by Django 4.0.5 on 2022-07-17 12:26
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        (
            "socialmedia",
            "0005_linkedinpost_api_delete_linkedinpost_api_deleted_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FacebookPost",
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
                ("post_id", models.CharField(max_length=30)),
            ],
        ),
    ]
