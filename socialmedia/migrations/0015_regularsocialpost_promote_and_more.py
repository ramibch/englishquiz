# Generated by Django 4.0.5 on 2022-07-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0014_alter_telegrammessage_chat_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularsocialpost',
            name='promote',
            field=models.BooleanField(default=True, verbose_name='Promote in Linkedin'),
        ),
        migrations.AddField(
            model_name='scheduledsocialpost',
            name='promote',
            field=models.BooleanField(default=True, verbose_name='Promote in Linkedin'),
        ),
    ]
