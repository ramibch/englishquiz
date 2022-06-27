from time import sleep
import random
import requests
import telegram
import tweepy

from django.conf import settings

from celery import shared_task

from quiz.models import Quiz, Lection, Question
from utils.management import send_mail_to_admin

# If a post intent fails > notify the admin
# NEED TO SET UP EMAIL BACKEND FIRST
# extra_subject = 'Linkedin promotion FAILED'
# body_text = f'Response is not 201: {instance.full_url} \n {response}'
# send_mail_to_admin(extra_subject=extra_subject, body_text=body_text)

# General variables and functions

common_hashtags = "#english #learnenglish #improveyourenglish #englishquiz #englishquizzes"

def escape_html_for_telegram(text):
    text.replace("<", "&lt;")
    text.replace(">", "&gt;")
    text.replace("&", "&amp;")
    return text

def get_hashtag_str_from_post_instance_tags(instance):
    hashtag_str = ''
    for tag in instance.tags.all():
        hashtag_str += '#'+tag.name + ' '
    return hashtag_str

def get_cool_random_emoji():
    cool_emojis = ["🤙", "😎", "🙃", "🤟"]
    return random.choice(cool_emojis)


def get_salutation_text():
    salutation_options = ["Hey there!", "Hey, how is it going?", "Hi!", "Hey!", "Hey, what's up?"]
    return random.choice(salutation_options)


def post_text_in_twitter(text):
    # API keys
    api_key = settings.TWITTER_API_KEY
    api_secret = settings.TWITTER_API_KEY_SECRET
    access_token = settings.TWITTER_ACCESS_TOKEN
    access_secret = settings.TWITTER_ACCESS_TOKEN_SECRET

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Tweet intent
    api.update_status(status=text)


def post_text_in_telegram(text):
    parsed_text = escape_html_for_telegram(text)
    telegram_account = settings.TELEGRAM_ACCOUNT
    api_key = telegram_account["BOT_API_KEY"]
    channel = telegram_account["CHANNEL_NAME"]
    bot = telegram.Bot(token=api_key)
    bot.send_message(chat_id=channel, text=parsed_text,
        parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=False)


def post_text_in_linkedin(text):
    # scope: w_member_social,r_liteprofile
    profile_id = settings.LINKEDIN_PROFILE_ID
    access_token = settings.LINKEDIN_ACCESS_TOKEN

    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {'Content-Type': 'application/json',
               'X-Restli-Protocol-Version': '2.0.0',
               'Authorization': 'Bearer ' + access_token}

    post_data = {
        "author": "urn:li:person:"+profile_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, json=post_data)

    return response


# Blog post tasks

def get_post_promotion_text(instance):
    """
    It generates text from a instance post
    """
    hashtags_from_instance_tags = get_hashtag_str_from_post_instance_tags(instance)
    text = f'✍️ New post: {instance.title} \n\n'
    text += f'{instance.full_url} \n \n'
    text += f'{hashtags_from_instance_tags}'
    return text


@shared_task(bind=True)
def promote_post_instance_in_telegram(self, instance):
    """
    Promote post instance in Telegram
    """
    try:
        text = get_post_promotion_text(instance)
        parsed_text = escape_html_for_telegram(text)
        post_text_in_telegram(parsed_text)

    except Exception as e:
        pass


@shared_task(bind=True)
def promote_post_instance_in_linkedin(self, instance):
    """
    Promote post instance in Linkedin
    """
    try:
        text = get_post_promotion_text(instance)
        response = post_text_in_linkedin(text)

        if not response.status_code == 201:
            pass

    except Exception as e:
        pass


@shared_task(bind=True)
def promote_post_instance_in_twitter(self, instance):
    """
    Promote post instance in Twitter
    """
    try:
        text = get_post_promotion_text(instance)
        post_text_in_twitter(text)

    except Exception as e:
        pass



# Quiz, Lection and Question tasks


def get_quiz_promotion_text(instance):
    """
    It generates text from a quiz instance
    """
    text = f'Check out this quiz: {instance.name} \n \n'
    text += f'👉 englishstuff.online{instance.get_detail_url()} \n \n'
    text += f'#english #learnenglish #{instance.name.replace(" ", "")}'
    return text


def get_question_text(instance):
    """
    It generates text from a question instance
    """
    text = ""
    if instance.type == 1 or instance.type == 5:
        text += "Here a small question for you. \n\n"
    if instance.type == 1:
        text += f"What do you think that comes in the gap? 🤔\n\n"
        text += f"📚 {instance.text_one} ____ {instance.text_two}"
        if instance.text_three:
            text += f" ____ {instance.text_three}\n"
    if instance.type == 5:
        text += f"What do you think is the right answer? 🤔\n\n"
        text += f"📚 {instance.text_one}\n\n"
        text += f"💡 Options:\n"
        for answer in instance.answer_set.all():
            text += f" 🔹 {answer.name}\n"

    return text


def get_question_promotion_text(instance):
    """
    It generates text from a question instance
    """
    salutation_text = get_salutation_text()
    cool_emoji = get_cool_random_emoji()
    question_text = get_question_text(question)

    # Producing text
    text = f"{salutation_text} {cool_emoji} \n\n"
    text += f'{question_text} \n\n'
    text += f'Check out the right answer here:\n'
    text += f'👉 englishstuff.online{instance.get_detail_url()} \n \n'
    text += f'#english #learnenglish #{instance.lection.quiz.replace(" ", "")}'

    return text



@shared_task(bind=True)
def promote_quiz_instance(self, **kwargs):
    try:
        instance = Quiz.objects.get(pk=kwargs["pk"])
        text = get_quiz_promotion_text(instance)
        post_text_in_telegram(text)
        post_text_in_linkedin(text)
        post_text_in_twitter(text)

    except Exception as e:
        pass


@shared_task(bind=True)
def promote_lection_instance(self, **kwargs):
    try:
        instance = Lection.objects.get(pk=kwargs["pk"])

        # Actually we promote the first question object (instance.get_first_question) of the lection instance
        text = get_question_promotion_text(instance.get_first_question())

        # promoting
        post_text_in_telegram(text)
        post_text_in_linkedin(text)
        post_text_in_twitter(text)

    except Exception as e:
        raise e


@shared_task(bind=True)
def share_random_question_instance(self, **kwargs):
    try:
        # Getting random question
        questions = Question.objects.filter(shared_in_social_media=False)
        question = random.choice(list(questions))

        if question:
            # Sharing
            post_text_in_telegram(text)
            post_text_in_linkedin(text)
            post_text_in_twitter(text)

            # Sleep 1 min after sharing 
            sleep(60)

            # Setting field shared_in_social_media to True -> so the question cannot be reshared
            question.shared_in_social_media=True
            question.save()
    except Exception as e:
        raise e
