from django.urls import path, include, re_path
from rest_framework import routers

from . import API_views

router = routers.SimpleRouter()
router.register('users', API_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_dashboard/', API_views.UserDashboardView.as_view(), name='api_user_dashboard'),
    path('roles/', API_views.RoleViewSet.as_view({'get': 'list'}), name='role_list'),
    path('register/', API_views.RegisterUserView.as_view(), name='api_register'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]