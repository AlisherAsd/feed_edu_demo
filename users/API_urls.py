from django.urls import path, include
from rest_framework import routers

from . import API_views

router = routers.SimpleRouter()
router.register('users', API_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user_dashboard/', API_views.UserDashboardView.as_view(), name='api_user_dashboard'),
    path('roles/', API_views.RoleViewSet.as_view({'get': 'list'}), name='role_list'),
]