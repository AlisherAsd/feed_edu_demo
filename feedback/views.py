from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model

from feedback.utils import get_data
from .forms import FeedbackForm, QuestionForm, AnswerForm
from .models import Feedback, Question, FeedbackType, Answer

menu = [
    {'title': 'Запросить', 'url': 'test_constructor'},
    {'title': 'Исходящие запросы', 'url': 'my_tests'},
    {'title': 'Личная страница', 'url': 'user_dashboard'},
    {'title': 'Входящие запросы', 'url': 'available_tests'},
    {'title': 'Пользователи', 'url': 'users'},
]


class test_constructor(View):
    def get(self, request):
        form_feedback = FeedbackForm()
        form_question = QuestionForm()
        print(request.GET)
        data = {
            'title': 'Создать новый фидбэк',
            'menu': menu,
            'form_feedback': form_feedback,
            'form_question': form_question
        }
        return render(request, 'feedback/test_constructor.html', context=data)
    def post(self, request):
        form_feedback = FeedbackForm(request.POST)
        form_question = QuestionForm(request.POST)
        if form_feedback.is_valid() and form_question.is_valid():

            create_obj1 = form_feedback.save(user=request.user)
            form_feedback.save_m2m()
            feedback_id = create_obj1.id
            form_question.save(feedback=Feedback.objects.get(id=feedback_id))

            return render(request, 'feedback/feedback_done.html')
        else:
            return HttpResponse("Ошибка")
        data = {
            'title': 'Создать новый фидбэк',
            'menu': menu,
            'form': form,
        }
        return render(request, 'feedback/test_constructor.html', context=data)


class my_tests(View):
    def get(self, request):
        feedbacks = Feedback.objects.filter(sender_id = request.user.id)
        answers = Answer.objects.all()
        data = {
            'title': 'Исходящие запросы',
            'menu': menu,
            'feedbacks': feedbacks,
            'answers': answers
        }
        return render(request, 'feedback/my_tests.html', context=data)


class available_tests(View):
    def get(self, request):

        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        feedbacks = user.received_feedbacks.all()
        questions = Question.objects.all()
        type_feedback = FeedbackType.objects.all()
        data = {
            'title': 'Входящие запросы',
            "menu": menu,
            "feedbacks": feedbacks,
            'questions': questions,
            'type_feedback': type_feedback
        }
        return render(request, 'feedback/available_tests.html', context=data)

@login_required
def get_question(request):
    if request.method == "GET":
        form = QuestionForm()
        return  render(request, 'feedback/question.html', {'form': form})
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_constructor')
        else:
            return HttpResponse("Ошибка")



def get_answer(request):
    if request.method == "GET":
        form = AnswerForm()
        data = {
            'title': 'Answer',
            'form': form
        }
    if request.method == "POST":
        form = AnswerForm(request.POST)
        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        print(request.POST)
        if form.is_valid():
            form.save(respondent=user)
            return redirect('available_tests')
        else:
            return HttpResponse("Ошибка, что-то с полями не так")
    return render(request, 'feedback/answer.html', context=data)