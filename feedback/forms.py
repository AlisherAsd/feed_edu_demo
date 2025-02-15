from django import forms
from .models import Feedback, User, Question, Answer


class FeedbackForm(forms.ModelForm):

    recipient = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Feedback
        fields = ['title', 'description', 'recipient', 'type']

    def save(self, commit=True, user=None):
        feedback = super().save(commit=False)  # Создайте объект без сохранения в БД
        if user is not None:
            feedback.sender = user  # Установите поле sender на аутентифицированного пользователя
        if commit:
            feedback.save()  # Сохраните объект в БД
        return feedback


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'type']

    def save(self, commit=True, feedback=None):
        question = super().save(commit=False)
        if feedback is not None:
            question.feedback = feedback
        if commit:
            question.save()
        return question


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['value', 'question']


    def save(self, commit=True, respondent=None):
        answer = super().save(commit=False)
        if respondent is not None:
            answer.respondent = respondent
        if commit:
            answer.save()
        return answer
