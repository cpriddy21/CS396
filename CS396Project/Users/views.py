#from django.shortcuts import render
#from django.views import generic
#from django.contrib.auth.forms import UserCreationForm
#from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User
from .forms import StudentSignUpForm, TeacherSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import student_required, teacher_required
# Create your views here.

#class UserRegisterView(generic.CreateView):
#    form_class = UserCreationForm
#    template_name = 'registration/register.html'
#    success_url = reverse_lazy('login')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'users/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student-home')
    
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'users/teacher_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teacher-home')
    
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_student:
                return reverse('student-home')
            elif user.is_teacher:
                return reverse('teacher-home')
        else:
            return reverse('login')
