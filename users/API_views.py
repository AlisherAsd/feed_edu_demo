from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from tutorial.quickstart.serializers import UserSerializer

from feedback.serializers import RoleSerializer
from .models import User, Role
from .serializers import UserListSerializer

import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    logger.debug('')
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    logger.debug('')
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAdminUser,)

class UserDashboardView(APIView):
    logger.debug('')
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        role = Role.objects.get(id=user.role_id)

        return Response({'user': UserListSerializer(user).data, 'role': RoleSerializer(role).data})

