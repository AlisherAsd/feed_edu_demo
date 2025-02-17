from django.urls import path, include
from rest_framework import routers

from . import API_views

# router = routers.SimpleRouter()
# router.register('my_tests', API_views.FeedbackViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('my_tests/', API_views.FeedbackApiView.as_view(), name='feedbacks'),
    path('available_tests/', API_views.FeedbackAvailableApiView.as_view(), name='feedbacks_available'),
    path('test_constructor/', API_views.FeedbackConstructorApiView.as_view(), name='test_constructor_api'),
    path('feedbacks/', API_views.FeedbackViewSet.as_view({'get': 'list'}), name='feedbacks'),
    path('type_feedbacks/', API_views.TypeFeedbackViewSet.as_view({'get': 'list'}), name='type_feedbacks'),
    path('type_question/', API_views.TypeQuestionViewSet.as_view({'get': 'list'}), name='type_questions'),
    path('answer/', API_views.AnswerApiView.as_view(), name='answer'),
]