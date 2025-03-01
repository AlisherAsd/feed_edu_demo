from django.db import models

from users.models import User


class Feedback(models.Model):
    """ Опросник имеет тип, множество вопросов, множество принимателей, отправителя """
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_feedback')
    recipient = models.ManyToManyField(User, related_name='received_feedbacks')
    type = models.ForeignKey('FeedbackType', on_delete=models.CASCADE, null=True)

class Question(models.Model):
    """ Вопрос имеет тип, один опросник """
    title = models.CharField(max_length=30)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    type = models.ForeignKey('QuestionType', on_delete=models.CASCADE, null=True)

class QuestionType(models.Model):
    """ Тип для вопроса """
    title = models.CharField(max_length=30)

class FeedbackType(models.Model):
    """ Тип для опросника """
    title = models.CharField(max_length=30)

class Answer(models.Model):
    """ Ответ на вопрос, имеет одного отправителя, и один вопрос """
    value = models.CharField(max_length=500)
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


