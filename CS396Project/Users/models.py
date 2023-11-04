from django.apps import apps
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from OnlineLearningSystem.models import Course

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    def enrolled_courses(self):
        Course = apps.get_model('OnlineLearningSystem', 'Course')  # Use apps.get_model to get the Course model
        return Course.objects.filter(students=self)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #batch = models.CharField(max_length=100)
    #roll_no = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

