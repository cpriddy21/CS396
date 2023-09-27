from django.contrib import admin

# Register your models here.
from .models import Post, Question, PracticeQuiz, Choice, QuizResult



admin.site.register(Post)
admin.site.register(PracticeQuiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizResult)