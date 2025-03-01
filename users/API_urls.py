from django.urls import path, include, re_path
from rest_framework import routers

from . import API_views

# Урлы для django rest users

router = routers.SimpleRouter()
router.register('users', API_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)), # Все юзеры
    path('user_dashboard/', API_views.UserDashboardView.as_view(), name='api_user_dashboard'), # Страница пользователя
    path('roles/', API_views.RoleViewSet.as_view({'get': 'list'}), name='role_list'), # Все роли (для админа и фронта)
    path('register/', API_views.RegisterUserView.as_view(), name='api_register'), # Страница регистрации (переопредлил тк модель юзера расщиренная)
    path('auth/', include('djoser.urls')), # Ауторизация через библиотек djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]