import random

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import never_cache
from django_htmx.http import trigger_client_event

from .models import Quiz, Lection, Question, Answer


@cache_page(3600 * 24)
def quiz_list(request):
    quiz_list = Quiz.objects.all()
    context ={'quiz_list': quiz_list}
    return render(request, 'quiz_list.html', context)


@cache_page(3600 * 6)
def quiz_detail(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug)
    lections = quiz.lection_set.all()
    context ={'quiz':quiz, 'lections': lections}
    return render(request, 'quiz_detail.html', context)


@cache_page(3600 * 6)
def question_detail(request, slug_quiz, slug_lection, id_question):
    quiz = get_object_or_404(Quiz, slug=slug_quiz)
    lection = get_object_or_404(Lection, slug=slug_lection, quiz=quiz)
    question = get_object_or_404(Question, id=id_question, lection=lection)
    questions = list(Question.objects.filter(lection=lection))
    index = questions.index(question)
    number_of_questions = questions.__len__()
    progress_percentage = int(index*100/number_of_questions)
    context ={'question': question, 'progress_percentage': progress_percentage}
    return render(request, 'question_detail.html', context)


@never_cache
def check_answer(request, slug_quiz, slug_lection, id_question):
    question = get_object_or_404(Question, id=id_question)

    if question.type == 1: # one choice selection
        selected_answer_id = request.POST.get('selected_answer_id')
        selected_answer = get_object_or_404(Answer, id=selected_answer_id)
        question_answered_correcty = selected_answer.correct
        context = {'question': question, 'selected_answer': selected_answer}
    elif question.type == 2: # multiple choice selection
        pass
    elif question.type == 3: # text input (one or two inputs)
        question_input_one = request.POST.get('question_input_one')
        answers = question.answer_set.all()
        if answers.count() > 1:
            question_input_two = request.POST.get('question_input_two')
            question_answered_correcty = answers[0].name.strip()==question_input_one.strip() and answers[1].name.strip()==question_input_two.strip()
            context = {'question': question, 'question_input_one': question_input_one, 'question_input_two': question_input_two}
        else:
            question_answered_correcty = answers[0].name.strip()==question_input_one.strip()
            context = {'question': question, 'question_input_one': question_input_one}

    if question_answered_correcty == True:
        correct_messages = ["Great!", "Correct!", "Well done!", "Terrific!", "Fantastic!", "Excelent!", "Super!", "Marvellous!", "Outstanding!",  ":)"]
        context['correct_message'] = random.choice(correct_messages)
        response = render(request, 'partials/question_correct.html', context)
    else:
        incorrect_messages = ["Next time you'll get it!", "There's a more accurate answer!", "Oops!", "Wrong :(", "Not quite correct!", ":("]
        context['incorrect_message'] = random.choice(incorrect_messages)
        response = render(request, 'partials/question_incorrect.html',  context)

    trigger_client_event(response, "answerCheckedEvent", { },) # this is the trigger event
    return response


@cache_page(3600 * 6)
def update_progress_bar(request, slug_quiz, slug_lection, id_question):
    quiz = get_object_or_404(Quiz, slug=slug_quiz)
    lection = get_object_or_404(Lection, slug=slug_lection, quiz=quiz)
    question = get_object_or_404(Question, id=id_question, lection=lection)
    questions = list(Question.objects.filter(lection=lection))
    index = questions.index(question) + 1
    number_of_questions = questions.__len__()
    progress_percentage = int(index*100/number_of_questions)
    context ={'progress_percentage': progress_percentage}
    return render(request, 'partials/progress_bar.html', context)
