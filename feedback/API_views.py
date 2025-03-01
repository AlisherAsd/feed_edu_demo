from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .serializers import FeedbackSerializer, QuestionSerializer, AnswerSerializer, TypeFeedbackSerializer, TypeQuestionSerializer
import logging

from feedback.models import Feedback, FeedbackType, QuestionType, Question, Answer

logger = logging.getLogger(__name__)


class FeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    """ Все опросники """
    logger.debug('')
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAdminUser, )

class TypeFeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    """ Все типы опросников """
    logger.debug('')
    serializer_class = TypeFeedbackSerializer
    queryset = FeedbackType.objects.all()
    permission_classes = (IsAdminUser,)

class TypeQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    """ Все типы вопросов """
    logger.debug('')
    serializer_class = TypeQuestionSerializer
    queryset = QuestionType.objects.all()
    permission_classes = (IsAdminUser,)

class FeedbackApiView(APIView):
    """ Все отправленные пользователям опросники """
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        feedbacks = Feedback.objects.filter(sender_id=request.user.id)
        return Response(FeedbackSerializer(feedbacks, many=True).data)

class FeedbackDetailApiView(APIView):
    """ Один отправленный пользователям опросники """
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        feedback_id = kwargs.get('id')
        feedback = get_object_or_404(Feedback, sender_id=request.user.id, pk=feedback_id)
        return Response(FeedbackSerializer(feedback).data, status=status.HTTP_200_OK)

class FeedbackAvailableApiView(APIView):
    """ Присланные опросники """
    logger.debug('')
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        feedbacks = user.received_feedbacks.all()
        return Response(FeedbackSerializer(feedbacks, many=True).data)

class FeedbackConstructorApiView(APIView):
    """ Создание опросника """

    permission_classes = (IsAuthenticated,)


    def post(self, request):
        # Получаем данные из запроса
        feedback_data = request.data.get('feedback')
        if not feedback_data:
            return Response({'error': 'Feedback data is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем существование sender и recipient
        sender_id = feedback_data.get('sender')
        recipient_ids = feedback_data.get('recipient', [])

        try:
            sender = User.objects.get(id=sender_id)
        except User.DoesNotExist:
            return Response({'error': f'Sender with ID {sender_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        for recipient_id in recipient_ids:
            try:
                recipient = User.objects.get(id=recipient_id)
            except User.DoesNotExist:
                return Response({'error': f'Recipient with ID {recipient_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

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
    """ Создание ответа """
    permission_classes = (IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        """ Создание ответов на id просника """
        feedback_id = kwargs.get('id')  # Получаем ID фидбека из URL
        user_id = request.user.id  # Получаем ID текущего пользователя

        # Получаем все вопросы для данного фидбека
        questions = Question.objects.filter(feedback_id=feedback_id)
        if not questions.exists():
            return Response({"error": "Вопросы для данного фидбека не найдены"}, status=status.HTTP_404_NOT_FOUND)

        # Проверяем, что количество ответов совпадает с количеством вопросов
        answers_data = request.data
        if not isinstance(answers_data, list):
            return Response({"error": "Ожидается список ответов"}, status=status.HTTP_400_BAD_REQUEST)

        if len(answers_data) != questions.count():
            return Response({"error": "Количество ответов не совпадает с количеством вопросов"}, status=status.HTTP_400_BAD_REQUEST)

        # Создаем список ответов с привязкой к вопросам
        answers_to_create = []
        for i, answer_data in enumerate(answers_data):
            answer_data['respondent'] = user_id
            answer_data['question'] = questions[i].id  # Привязываем ответ к вопросу
            answers_to_create.append(answer_data)

        # Сериализуем и сохраняем ответы
        serializer = AnswerSerializer(data=answers_to_create, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """ Получение ответов на id просника """
        feedback_id = kwargs.get('id')  # Получаем ID фидбека из URL
        my_feedback_answer = Feedback.objects.filter(id=feedback_id, sender_id=request.user.id)

        if not my_feedback_answer.exists():
            return Response({"error": "У вас нет такого опросника"}, status=status.HTTP_404_NOT_FOUND)

        # Получаем все вопросы для данного фидбека
        questions = Question.objects.filter(feedback_id=feedback_id)

        if not questions.exists():
            return Response({"error": "Вопросы для данного фидбека не найдены"}, status=status.HTTP_404_NOT_FOUND)

        # Получаем все ответы, связанные с этими вопросами
        answers = Answer.objects.filter(question__in=questions)

        # Сериализуем ответы
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)