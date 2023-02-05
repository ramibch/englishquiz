# Generated by Django 4.0.9 on 2023-02-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0009_alter_bookaffiliatelink_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, unique=True),
        ),
    ]
