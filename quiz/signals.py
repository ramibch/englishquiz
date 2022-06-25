
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Quiz, Lection

from sharing import tasks as sharing_tasks


@receiver(post_save, sender=Quiz)
def schedule_promoting_quiz(sender, instance, **kwargs):
    if instance.promote and not instance.already_promoted:
        sharing_tasks.promote_quiz_instance_in_telegram.apply_async(eta=instance.promote_date, kwargs={"pk":instance.pk})
        sharing_tasks.promote_quiz_instance_in_linkedin.apply_async(eta=instance.promote_date, kwargs={"pk":instance.pk})
        sharing_tasks.promote_quiz_instance_in_twitter.apply_async(eta=instance.promote_date, kwargs={"pk":instance.pk})
        instance.already_promoted = True
        instance.save()


@receiver(post_save, sender=Lection)
def schedule_promoting_lection(sender, instance, **kwargs):
    if instance.promote and not instance.already_promoted:
        sharing_tasks.promote_lection_instance_in_telegram.apply_async(eta=instance.promote_date, kwargs={"pk":instance.pk})
        sharing_tasks.promote_lection_instance_in_linkedin.apply_async(eta=instance.promote_date, kwargs={"pk":instance.pk})
        sharing_tasks.promote_lection_instance_in_twitter.apply_async(eta=instance.promote_date, kwargs={"pk":instance.pk})
        instance.already_promoted = True
        instance.save()
