# Generated by Django 4.2 on 2023-04-20 20:04
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_flexpage_contact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="flexpage",
            options={
                "base_manager_name": "prefetch_manager",
                "ordering": ("-created",),
            },
        ),
    ]
