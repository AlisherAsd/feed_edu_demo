from django.contrib.auth import get_user_model
from django.http import request
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FeedbackSerializer

from feedback.models import Feedback


class FeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

class FeedbackApiView(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.filter(sender_id=request.user.id)
        return Response(FeedbackSerializer(feedbacks, many=True).data)


class FeedbackAvailableApiView(APIView):
    def get(self, request):
        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        feedbacks = user.received_feedbacks.all()
        return Response(FeedbackSerializer(feedbacks, many=True).data)

class FeedbackConstructorApiView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(FeedbackSerializer(serializer.instance).data)