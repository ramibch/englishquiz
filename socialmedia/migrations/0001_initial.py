# Generated by Django 4.0.5 on 2022-07-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegularSocialPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('image_text', models.TextField(blank=True, max_length=200, null=True)),
                ('promote', models.BooleanField(default=True, verbose_name='Promote in Linkedin')),
                ('promote_in_linkedin', models.BooleanField(default=True, verbose_name='Promote in Linkedin')),
                ('promote_in_twitter', models.BooleanField(default=True, verbose_name='Promote in Twitter')),
                ('promote_in_telegram', models.BooleanField(default=True, verbose_name='Promote in Telegram')),
                ('promote_in_facebook', models.BooleanField(default=False, verbose_name='Promote in Facebook')),
                ('promote_in_instagram', models.BooleanField(default=False, verbose_name='Promote in Instagram')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('promoted', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduledSocialPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('image_text', models.TextField(blank=True, max_length=200, null=True)),
                ('promote', models.BooleanField(default=True, verbose_name='Promote in Linkedin')),
                ('promote_in_linkedin', models.BooleanField(default=True, verbose_name='Promote in Linkedin')),
                ('promote_in_twitter', models.BooleanField(default=True, verbose_name='Promote in Twitter')),
                ('promote_in_telegram', models.BooleanField(default=True, verbose_name='Promote in Telegram')),
                ('promote_in_facebook', models.BooleanField(default=False, verbose_name='Promote in Facebook')),
                ('promote_in_instagram', models.BooleanField(default=False, verbose_name='Promote in Instagram')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('promote_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaPostedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_id', models.CharField(blank=True, max_length=20, null=True)),
                ('instagram_id', models.CharField(blank=True, max_length=20, null=True)),
                ('linkedin_likes', models.IntegerField(blank=True, null=True)),
                ('telegram_id', models.CharField(blank=True, max_length=20, null=True)),
                ('telegram_likes', models.IntegerField(blank=True, null=True)),
                ('tweet', models.CharField(blank=True, max_length=20, null=True)),
                ('twitter_likes', models.IntegerField(blank=True, null=True)),
                ('facebook_id', models.CharField(blank=True, max_length=20, null=True)),
                ('facebook_likes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField()),
                ('message_id', models.BigIntegerField()),
                ('link', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=4000)),
                ('date', models.DateTimeField()),
                ('api_delete', models.BooleanField(default=False, help_text='It gets deleted from Telegram after clicking on Save', verbose_name='Delete from Telegram')),
                ('api_deleted', models.BooleanField(default=False, verbose_name='Already deleted from Telegram')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.PositiveIntegerField()),
                ('id_str', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=300)),
                ('twitter_url', models.URLField(null=True)),
                ('created_at', models.DateTimeField()),
                ('retweet_count', models.PositiveIntegerField()),
                ('favorite_count', models.PositiveIntegerField()),
                ('api_delete', models.BooleanField(default=False, help_text='It gets deleted from Twitter after clicking on Save', verbose_name='Delete from Twitter')),
                ('api_deleted', models.BooleanField(default=False, verbose_name='Already deleted from Twitter')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn_li_share', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('click_count', models.PositiveIntegerField(null=True)),
                ('comment_count', models.PositiveIntegerField(null=True)),
                ('engagement', models.FloatField(null=True)),
                ('impression_count', models.PositiveIntegerField(null=True)),
                ('like_count', models.PositiveIntegerField(null=True)),
                ('share_count', models.PositiveIntegerField(null=True)),
            ],
        )
    ]
