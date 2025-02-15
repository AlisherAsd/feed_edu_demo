from django.contrib import admin

from feedback.models import Feedback, QuestionType, FeedbackType, Question, Answer

admin.site.register(Feedback)
admin.site.register(QuestionType)
admin.site.register(FeedbackType)
admin.site.register(Question)
admin.site.register(Answer)
