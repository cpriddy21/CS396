from django import template
from OnlineLearningSystem.models import Course

register = template.Library()

@register.inclusion_tag('courses_dropdown.html')
def courses_dropdown(user):
    all_courses = Course.objects.all()
    return {'all_courses': all_courses}