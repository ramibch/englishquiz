# Generated by Django 4.0.8 on 2023-02-04 21:20

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0007_alter_book_options_book_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=5)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('-views',),
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='bookaffiliatelink',
            name='label',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
