#from django.contrib import admin
#from django.urls import path
#from .views import UserRegisterView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('register/',UserRegisterView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/student/", views.StudentSignUpView.as_view(), name="student-signup"),
    path("signup/teacher/", views.TeacherSignUpView.as_view(), name="teacher-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]