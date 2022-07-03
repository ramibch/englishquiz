# Generated by Django 4.0.5 on 2022-07-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0003_delete_largesocialpost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularsocialpost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='regularsocialpost',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='scheduledsocialpost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='scheduledsocialpost',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='regularsocialpost',
            name='promoted',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
