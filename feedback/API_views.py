from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FeedbackSerializer, QuestionSerializer, AnswerSerializer
import logging

from feedback.models import Feedback


logger = logging.getLogger(__name__)


class FeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    logger.debug('')
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAdminUser, )

class TypeFeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    logger.debug('')
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAdminUser,)

class TypeQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    logger.debug('')
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAdminUser,)


class FeedbackApiView(APIView):
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        feedbacks = Feedback.objects.filter(sender_id=request.user.id)
        return Response(FeedbackSerializer(feedbacks, many=True).data)


class FeedbackAvailableApiView(APIView):
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        feedbacks = user.received_feedbacks.all()
        return Response(FeedbackSerializer(feedbacks, many=True).data)

class FeedbackConstructorApiView(APIView):
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        # Получаем данные из запроса
        feedback_data = request.data.get('feedback')

        # Сериализуем данные для Feedback
        feedback_serializer = FeedbackSerializer(data=feedback_data)
        feedback_serializer.is_valid(raise_exception=True)
        feedback_instance = feedback_serializer.save()

        # Обрабатываем вопросы, если они есть
        questions_data = feedback_data.get('questions', [])
        for question_data in questions_data:
            question_data['feedback'] = feedback_instance.id  # Устанавливаем связь с созданным Feedback
            question_serializer = QuestionSerializer(data=question_data)
            question_serializer.is_valid(raise_exception=True)
            question_serializer.save()

        # Возвращаем созданный Feedback и связанные Questions
        return Response(feedback_serializer.data, status=status.HTTP_201_CREATED)


class AnswerApiView(APIView):
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
