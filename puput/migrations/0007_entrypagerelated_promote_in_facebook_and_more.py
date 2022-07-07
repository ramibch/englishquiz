# Generated by Django 4.0.5 on 2022-07-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puput', '0006_alter_tagentrypage_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrypagerelated',
            name='promote_in_facebook',
            field=models.BooleanField(default=True, verbose_name='Promote in Facebook'),
        ),
        migrations.AddField(
            model_name='entrypagerelated',
            name='promote_in_instagram',
            field=models.BooleanField(default=True, verbose_name='Promote in Instagram'),
        ),
        migrations.AddField(
            model_name='entrypagerelated',
            name='promote_in_linkedin',
            field=models.BooleanField(default=True, verbose_name='Promote in Linkedin'),
        ),
        migrations.AddField(
            model_name='entrypagerelated',
            name='promote_in_telegram',
            field=models.BooleanField(default=True, verbose_name='Promote in Telegram'),
        ),
        migrations.AddField(
            model_name='entrypagerelated',
            name='promote_in_twitter',
            field=models.BooleanField(default=True, verbose_name='Promote in Twitter'),
        ),
    ]
