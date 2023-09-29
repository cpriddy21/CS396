from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from Users.models import User
from django.urls import reverse
from datetime import datetime, date
#from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    #title_tag = models.CharField(max_length=255, default="Title")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()#RichTextField(blank=True, null=True)
    image = models.ImageField(null = True, blank = True, upload_to="images/")
    video = models.FileField(null=True, blank=True, upload_to="videos/")


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
       return reverse("home")
       #return reverse("post-detail", args=(str(self.pk)))

class PracticeQuiz(models.Model):
    title = models.CharField(max_length=100)
    question_count = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000, default='')
    def __str__(self):
        return self.title 

class Question(models.Model):
    quiz = models.ForeignKey(PracticeQuiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    def __str__(self):
        return str(self.quiz) + ' | ' + self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return str(self.question) + ' | ' + self.text

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(PracticeQuiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return {self.user.username} + '\'s result for' + {self.quiz.title}

