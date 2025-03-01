from django.urls import path, include
from rest_framework import routers

from . import API_views

# router = routers.SimpleRouter()
# router.register('my_tests', API_views.FeedbackViewSet)

# Урлы для rets приложения

urlpatterns = [
    # path('', include(router.urls)),
    path('my_tests/', API_views.FeedbackApiView.as_view(), name='feedbacks'), # Отправленные опросники
    path('available_tests/', API_views.FeedbackAvailableApiView.as_view(), name='feedbacks_available'), # Присланные опросники
    path('test_constructor/', API_views.FeedbackConstructorApiView.as_view(), name='test_constructor_api'), # Создание опросника
    path('feedbacks/', API_views.FeedbackViewSet.as_view({'get': 'list'}), name='feedbacks'), # Все опросники (для админа и фронта)
    path('feedbacks/<int:id>', API_views.FeedbackDetailApiView.as_view(), name='feedbacks_detail'), # Опросник
    path('type_feedbacks/', API_views.TypeFeedbackViewSet.as_view({'get': 'list'}), name='type_feedbacks'), # Все типы опросников (для админа и фронта)
    path('type_question/', API_views.TypeQuestionViewSet.as_view({'get': 'list'}), name='type_questions'), # Все типы вопросов (для админа и фронта)
    path('answer/<int:id>', API_views.AnswerApiView.as_view(), name='answer'), # Создание ответа
]