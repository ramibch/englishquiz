import random
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

QUIZ_LEVEL_CHOICES = (
    (1, 'A1'),
    (2, 'A2'),
    (3, 'B1'),
    (4, 'B2'),
    (5, 'C1'),
    (6, 'C2'),
)

QUESTION_TYPE_CHOICES = (
    (1, '1: One text input'),
    (2, '2: Two text input'),
    (5, '5: One choice selection'),
    (6, '6: Multiple choice selection'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=64)
    level = models.IntegerField(default=5, choices=QUIZ_LEVEL_CHOICES)
    slug = models.SlugField(blank=True, unique=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    image_credits_url = models.URLField(max_length=200, null=True)

    def get_detail_url(self):
        return reverse('quiz_detail', kwargs={'slug': self.slug})

    def get_list_url(self):
        return reverse('home')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Quiz, self).save(*args, **kwargs)


class Lection(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True, unique=True)

    # def get_number_of_questions(self):
    #     return self.question_set.all().count()

    def get_first_question(self):
        return self.question_set.all().first()

    def __str__(self):
        return f'{self.name} ({self.quiz.name})'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lection, self).save(*args, **kwargs)


class Question(models.Model):
    lection = models.ForeignKey(Lection, on_delete=models.CASCADE)
    text_one = models.CharField(max_length=200)
    text_two = models.CharField(max_length=150, null=True, blank=True)
    text_three = models.CharField(max_length=150, null=True, blank=True)
    type = models.IntegerField(default=1, choices=QUESTION_TYPE_CHOICES)
    explanation = models.CharField(max_length=250, blank=True, null=True)

    def get_detail_url(self):
        return reverse('question_detail', kwargs={'slug_quiz': self.lection.quiz.slug, 'slug_lection': self.lection.slug, 'id_question': self.id})

    def check_answer_url(self):
        return reverse('check_answer', kwargs={'slug_quiz': self.lection.quiz.slug, 'slug_lection': self.lection.slug, 'id_question': self.id})

    def update_progress_bar_url(self):
        return reverse('update_progress_bar', kwargs={'slug_quiz': self.lection.quiz.slug, 'slug_lection': self.lection.slug, 'id_question': self.id})

    def is_first(self):
        return self.__class__.objects.filter(lection=self.lection).first() == self

    def is_last(self):
        return self.__class__.objects.filter(lection=self.lection).last() == self

    def previous_object(self):
        return self.__class__.objects.filter(id__lt=self.id, lection=self.lection).order_by('id').last()

    def next_object(self):
        return self.__class__.objects.filter(id__gt=self.id, lection=self.lection).order_by('id').first()

    def __str__(self):
        return f'{self.lection.quiz.name} - {self.lection.name} - {self.text_one}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name
