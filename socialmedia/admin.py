from django.contrib import admin

from .models import (ScheduledSocialPost, 
                    RegularSocialPost, 
                    TelegramMessage,
                    TwitterPost
                    )



class ScheduledSocialPostAdmin(admin.ModelAdmin):
    search_fields = ['text']
    readonly_fields = ['created', 'updated']
    list_filter = ['created', 'updated']

class RegularSocialPostAdmin(admin.ModelAdmin):
    search_fields = ['text']
    readonly_fields = ['created', 'updated', 'promoted']
    list_filter = ['created', 'updated', 'promoted']


class TweetAdmin(admin.ModelAdmin):
    search_fields = ['text']
    readonly_fields = ['text', 'created_at', 'favorite_count', 'twitter_id', 'id_str', 'retweet_count', 'twitter_url', 'api_deleted']
    list_filter = ['created_at']
    list_display = ['text', 'twitter_id', 'retweet_count', 'favorite_count',]


class TelegramMessageAdmin(admin.ModelAdmin):
    search_fields = ['text']
    readonly_fields = ['text', 'message_id', 'chat_id', 'link', 'date', 'api_deleted']
    list_filter = ['date']
    # list_display = ['text', 'twitter_id', 'retweet_count', 'favorite_count',]



admin.site.register(ScheduledSocialPost, ScheduledSocialPostAdmin)
admin.site.register(RegularSocialPost, RegularSocialPostAdmin)


admin.site.register(TwitterPost, TweetAdmin)
admin.site.register(TelegramMessage, TelegramMessageAdmin)


