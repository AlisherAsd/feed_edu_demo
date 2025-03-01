from django.urls import path

from . import views

# Урлы для django template users
urlpatterns = [
    path("user_dashboard/", views.user_dashboard.as_view(), name="user_dashboard"), # Страница пользователя
    path("users/", views.users.as_view(), name="users"), # Все пользователи на сайте
    path("login/", views.login, name="login"), # Логин
    path("register/", views.register, name="register"), # Регистрация
    path("logout/", views.logout_user, name="logout"), # Выход
]