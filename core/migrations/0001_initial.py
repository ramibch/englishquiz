# Generated by Django 4.0.9 on 2023-02-16 21:39
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CountryVisitor",
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
                ("country_code", models.CharField(max_length=5)),
                ("views", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ("-views",),
            },
        ),
    ]
