# Generated by Django 4.0.5 on 2022-07-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0015_regularsocialpost_promote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='favorite_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='twitter_id',
            field=models.PositiveIntegerField(),
        ),
    ]
