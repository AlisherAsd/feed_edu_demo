from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from tutorial.quickstart.serializers import UserSerializer

from feedback.serializers import RoleSerializer
from .models import User, Role
from .serializers import UserListSerializer

from feedback.models import Feedback


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        role = Role.objects.get(id=user.role_id)

        return Response({'user': UserListSerializer(user).data, 'role': RoleSerializer(role).data})