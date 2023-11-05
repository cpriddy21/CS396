from django import template
from OnlineLearningSystem.models import Course
from Users.models import User

register = template.Library()

@register.inclusion_tag('courses_dropdown.html')
def courses_dropdown(request):
    if request.user.is_authenticated and request.user.is_student:
        courses = request.user.courses.all()
        #print("Enrolled courses:", enrolled_courses)
    if request.user.is_authenticated and request.user.is_teacher:
        courses = Course.objects.all()  # Add this line to fetch all courses
    # Filter quizzes based on the selected course, if provided
    all_courses = Course.objects.all()
    return {'all_courses': all_courses}