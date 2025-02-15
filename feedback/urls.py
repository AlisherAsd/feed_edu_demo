from django.urls import path

from . import views

urlpatterns = [
    path("test_constructor/", views.test_constructor.as_view(), name="test_constructor"),
    path("my_tests/", views.my_tests.as_view(), name="my_tests"),
    path("available_tests/", views.available_tests.as_view(), name="available_tests"),
    path("question/", views.get_question, name="question"),
    path("answer/", views.get_answer, name="answer"),
]