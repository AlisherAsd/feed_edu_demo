from rest_framework import serializers

from feedback.models import Feedback, FeedbackType, Question, QuestionType, Answer
from users.models import Role


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class TypeFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackType
        fields = '__all__'


class TypeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'