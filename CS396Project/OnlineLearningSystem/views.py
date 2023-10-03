from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Reply, PracticeQuiz, Question, Choice, QuizResult
from .forms import PostForm, ReplyForm, UpdatePostForm, QuizAnswerForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import get_messages
from datetime import datetime, timedelta

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

def quiz_results_view(request):
    # Query all quizzes and their associated results
    quizzes = PracticeQuiz.objects.all()
    quiz_results = []

    # Loop through each quiz and get the results for each user
    for quiz in quizzes:
        results = QuizResult.objects.filter(quiz=quiz)
        quiz_results.append({
            'quiz': quiz,
            'results': results
        })

    return render(request, 'quiz_results.html', {'quiz_results': quiz_results})

# def ActiveQuizView(request, quiz_pk):
#     if request.method == 'POST':
#         quiz = quiz.objects.get(pk=quiz_pk)
#         questions = Question.objects.filter(quiz=quiz)
#         total_score = 0

#         for question in questions:
#             correct = str(question.correct)

    

# def QuizView(request, quiz_pk):
#     try:
#         quiz = get_object_or_404(PracticeQuiz, pk=quiz_pk)
#     except:
#         return FileNotFoundError
#     questions = Question.objects.filter(quiz=quiz)

#     if request.method == 'POST':
#         form = QuizAnswerForm(request.POST)
#         if form.is_valid():
#             # Process and save the user's answers
#             print("Form is valid")
#             print(form.cleaned_data)
#             user = request.user
#             for question in questions:
#                 selected_choice = form.cleaned_data.get(f'question_{question.id}_selected_choice')
#                 print(selected_choice)
#                 QuizResult.objects.create(
#                     user=user,
#                     quiz=quiz,
#                     question=question,
#                     selected_choice=selected_choice,
#                     score=(1 if selected_choice.is_correct else 0),  # You can adjust the scoring logic
#                 )
#                 print("Form is valid - Quiz submitted successfully")
#             return redirect('quiz_results')  # Redirect to a page showing quiz results
#         else:
#             print("Form is not valid")
#             print(form.errors) 
#     else:
#         form = QuizAnswerForm()

#     return render(request, 'active_quiz.html', {'quiz': quiz, 'questions': questions, 'form': form})

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

class QuizListView(ListView):
    model = PracticeQuiz 
    template_name = 'quiz_list.html'
    ordering = ['-id']   

def pdf_viewer(request):
    return render(request, 'pdf_viewer.html')
