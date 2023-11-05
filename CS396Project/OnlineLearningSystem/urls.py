from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView
from .views import QuizView, QuizListView
urlpatterns = [
    #path('',views.home, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('Post/<slug>', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('Post/edit/<int:pk>', UpdatePostView.as_view(),name='update_post'),
    path('Post/<int:pk>/delete', DeletePostView.as_view(),name='delete_post'),
    #path('quiz_directory',QuizListView.as_view(), name='quiz_list'),
    path('quiz_directory/<int:course_id>/',QuizListView, name='quiz_list'),
    path('Quiz/<int:quiz_pk>', QuizView, name='quiz'),
    path('pdf_viewer/', views.pdf_viewer, name='pdf_viewer'),
    path('quiz_results/', views.quiz_results_view, name='quiz_results'),
    path('search/', views.search_results_view, name='search_results'),   
]