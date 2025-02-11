from django.urls import path

from . import views

urlpatterns = [
    path("user_dashboard/", views.user_dashboard.as_view(), name="user_dashboard"),
    path("users/", views.users.as_view(), name="users"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_user, name="logout"),
]