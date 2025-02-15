from django.urls import path, include
from rest_framework import routers

from . import API_views

# router = routers.SimpleRouter()
# router.register('my_tests', API_views.FeedbackViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('my_tests/', API_views.FeedbackApiView.as_view(), name='feedbacks'),
    path('available_tests/', API_views.FeedbackAvailableApiView.as_view(), name='feedbacks_available'),
    path('test_constructor/', API_views.FeedbackConstructorApiView.as_view(), name='feedbacks_available'),

]