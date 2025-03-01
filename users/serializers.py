from rest_framework import serializers

from feedback.models import User
from users.models import Role


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'avatar', 'role']

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'avatar', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'