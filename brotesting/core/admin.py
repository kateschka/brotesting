from django.contrib import admin
from .models import (
    Quiz, Question, Choice,
    QuizAttempt, StudentAnswer, QuizSettings, Course
)


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizAttempt)
admin.site.register(StudentAnswer)
admin.site.register(QuizSettings)
admin.site.register(Course)
