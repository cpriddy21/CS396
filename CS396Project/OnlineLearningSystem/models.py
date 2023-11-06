import uuid
from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from Users.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from autoslug import AutoSlugField
#from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title')
    #title_tag = models.CharField(max_length=255, default="Title")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()#RichTextField(blank=True, null=True)
    image = models.ImageField(null = True, blank = True, upload_to="images/")
    video = models.FileField(null=True, blank=True, upload_to="videos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
       return reverse("home")
       #return reverse("post-detail", args=(str(self.pk)))
    class Meta:
        app_label = 'OnlineLearningSystem'
        db_table = 'OnlineLearningSystem_post'

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name="replies", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()#RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post.title + ' reply | ' + str(self.author)
    
class Course(models.Model):
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150, null=True, blank=True, default=None)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User,related_name='courses')
    course_code = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    

    def __str__(self):
        return self.name
    
class PracticeQuiz(models.Model):
    title = models.CharField(max_length=100, unique=True)
    question_count = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000, default='')
    course = models.ForeignKey(Course, related_name="quizzes", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    attempts = models.PositiveIntegerField(default=3)
    def __str__(self):
        return self.title 

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey('PracticeQuiz', on_delete=models.CASCADE)
    attempts_left = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.user.username}'s attempt for {self.quiz.title}"


class Question(models.Model):
    quiz = models.ForeignKey(PracticeQuiz, related_name="questions", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    def __str__(self):
        return str(self.quiz) + ' | ' + self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return str(self.question) + ' | ' + self.text
    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "text")
        ]

class QuizResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(PracticeQuiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    score = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.username}'s result for {self.quiz.title}"
    