# Generated by Django 4.0.9 on 2023-02-16 22:06
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("affiliates", "0011_book_thumbnail_url"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CountryVisitor",
        ),
    ]
