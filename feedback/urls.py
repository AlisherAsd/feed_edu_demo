from django.urls import path

from . import views

# Урлы для django template
urlpatterns = [
    path("test_constructor/", views.test_constructor.as_view(), name="test_constructor"), # Создание опросника
    path("my_tests/", views.my_tests.as_view(), name="my_tests"), # Мои отправленные опросники
    path("available_tests/", views.available_tests.as_view(), name="available_tests"), # Пришедшие опросники
    path("question/", views.get_question, name="question"), # Адрес для создание вопроса (тестовый)
    path("answer/", views.get_answer, name="answer"), # Адрес для создание ответа (тестовый)
]