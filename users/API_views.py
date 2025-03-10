from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


from feedback.serializers import RoleSerializer
from .models import User, Role
from .serializers import UserListSerializer, RegisterSerializer

import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ Все юзеры """
    logger.debug('')
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    """ Все роли """
    logger.debug('')
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAdminUser,)

class UserDashboardView(APIView):
    """ Страница пользователя """
    logger.debug('')
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        role = Role.objects.get(id=user.role_id)

        return Response({'user': UserListSerializer(user).data, 'role': RoleSerializer(role).data})

class RegisterUserView(APIView):
    """ Сраница регистрации """
    logger.debug('')
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Хешируем пароль
            user.set_password(request.data.get('password'))
            user.save()  #
            return Response({'user': UserListSerializer(user).data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
