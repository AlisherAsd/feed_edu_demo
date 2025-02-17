from django.db import models

from users.models import User

# Сделать модель answer 1 : 1 c question, и 1 : N к users

class Feedback(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_feedback')
    recipient = models.ManyToManyField(User, related_name='received_feedbacks')
    type = models.ForeignKey('FeedbackType', on_delete=models.CASCADE, null=True)


class Question(models.Model):
    title = models.CharField(max_length=30)
    value = models.CharField(max_length=200)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    type = models.ForeignKey('QuestionType', on_delete=models.CASCADE, null=True)



class QuestionType(models.Model):
    title = models.CharField(max_length=30)

class FeedbackType(models.Model):
    title = models.CharField(max_length=30)

class Answer(models.Model):
    value = models.CharField(max_length=500)
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


