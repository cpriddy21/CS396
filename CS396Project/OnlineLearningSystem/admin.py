from django.contrib import admin

# Register your models here.
from .models import Post, Question, PracticeQuiz, Choice, QuizResult, Reply



admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(PracticeQuiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizResult)