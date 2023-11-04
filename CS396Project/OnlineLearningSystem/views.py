from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Reply, PracticeQuiz, Question, Choice, QuizResult, Course
from .forms import PostForm, ReplyForm, UpdatePostForm, QuizAnswerForm
from django.urls import reverse_lazy
from django.db.models import Sum, Q
from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import get_messages
from datetime import datetime, timedelta

# Create your views here.

# def courses_view(request):
#     return render(request, 'courses_view.html', {})
def QuizListView(request, course_id=None):
    all_courses = Course.objects.all()  # Add this line to fetch all courses
    # Filter quizzes based on the selected course, if provided
    if course_id is not None:
        quizzes = PracticeQuiz.objects.filter(course__id=course_id)
    else:
        # If no course is selected, show all quizzes
        quizzes = PracticeQuiz.objects.all()
    
    return render(request, 'quiz_list.html', {'quizzes': quizzes, 'all_courses': all_courses})

def search_results_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(
            Q(body__contains=searched) |
            Q(title__contains=searched) |
            Q(author__username__contains=searched) |
            Q(created_at__contains=searched)
        )
        return render(request, 'search_results.html', {'searched':searched, 'posts':posts})
        
    else:
        return render(request, 'search_results.html', {})

def quiz_results_view(request):
    # Query all quiz results
    quiz_results = QuizResult.objects.all()

    # Create a dictionary to store grouped results
    grouped_results = {}

    for result in quiz_results:
        key = (result.user.username, result.quiz.title)
        if key not in grouped_results:
            grouped_results[key] = {
                'user': result.user,
                'quiz_title': result.quiz.title,
                'total_score': 0,  # Initialize total score
                'total_results': 0,  # Initialize total number of results
            }
        grouped_results[key]['total_score'] += result.score
        grouped_results[key]['total_results'] += 1

    # Calculate the percentage score for each group
    for key, group in grouped_results.items():
        total_score = group['total_score']
        total_results = group['total_results']
        if total_results > 0:
            group['percentage_score'] = round((total_score / total_results) * 100)

    # Convert the dictionary values to a list
    grouped_results_list = grouped_results.values()

    return render(request, 'quiz_results.html', {'grouped_results': grouped_results_list})

def QuizView(request, quiz_pk):
    try:
        quiz = get_object_or_404(PracticeQuiz, pk=quiz_pk)
    except:
        return FileNotFoundError
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        # Create a dictionary to store user's answers for each question
        user_answers = {}

        for question in questions:
            field_name = f'question_{question.id}_selected_choice'
            selected_choice_id = request.POST.get(field_name)

            # Ensure a choice is selected for each question
            if selected_choice_id:
                user_answers[question.id] = selected_choice_id
            else:
                # Handle the case where a choice is not selected for a question
                # You can add error handling or messages here
                pass

        # Check if the user has provided answers for all questions
        if len(user_answers) == len(questions):
            # Process and save the user's answers
            user = request.user
            for question_id, selected_choice_id in user_answers.items():
                question = Question.objects.get(id=question_id)
                selected_choice = Choice.objects.get(id=selected_choice_id)
                QuizResult.objects.create(
                    user=user,
                    quiz=quiz,
                    question=question,
                    selected_choice=selected_choice,
                    score=(1 if selected_choice.is_correct else 0),  # You can adjust the scoring logic
                )
            return redirect('quiz_results')  # Redirect to a page showing quiz results
        else:
            # Handle the case where the user didn't answer all questions
            # You can add error handling or messages here
            pass

    # If the form is not valid or not all questions are answered, render the quiz page again
    form = QuizAnswerForm()  # You should create a QuizAnswerForm with the modified field names
    return render(request, 'active_quiz.html', {'quiz': quiz, 'questions': questions, 'form': form})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate the timestamp 5 minutes ago
        five_minutes_ago = datetime.now() - timedelta(minutes=5)

        # Count the number of posts created within the last 5 minutes
        new_posts_count = Post.objects.filter(created_at__gte=five_minutes_ago).count()

        context['new_posts_banner'] = f'There have been {new_posts_count} new posts in the last 5 minutes.'

        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    slug_field = 'slug'

    form = ReplyForm
    def post(self, request, *args, **kwargs):
        form = ReplyForm(request.POST) 
        if form.is_valid():
            post = self.get_object()
            if request.user.is_authenticated:
            
                post = self.get_object()
                form.instance.author = request.user
                form.instance.post = post
               
                form.save()

                return redirect(reverse("post-detail", kwargs={'slug': post.slug}))
            else:
                return redirect('login')
    def get_context_data(self, **kwargs):
        post_replies_count = Reply.objects.all().filter(post=self.object.id).count()
        post_replies = Reply.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form(),  # Pass user here
            'post_replies': post_replies,
            'post_replies_count': post_replies_count,
        })
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# class QuizListView(ListView):
#     model = PracticeQuiz 
#     template_name = 'quiz_list.html'
#     ordering = ['-id']   

def pdf_viewer(request):
    return render(request, 'pdf_viewer.html')


