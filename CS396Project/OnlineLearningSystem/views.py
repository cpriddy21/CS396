from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PracticeQuiz, Question, Choice, QuizResult
from .forms import PostForm
from django.urls import reverse_lazy
from .forms import PostForm, UpdatePostForm

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

def calculate_score(post_data, questions, selected_choices):
    total_score = 0
    for question in questions:
        selected_choice_id = post_data.get(f'question_{question.id}')
        if selected_choice_id:
            selected_choice = Choice.objects.get(id=selected_choice_id)
            if selected_choice.is_correct:
                total_score += 1  
            selected_choices[question.id] = selected_choice
    return total_score

def QuizView(request, quiz_pk):
    try:
        quiz = get_object_or_404(PracticeQuiz, pk=quiz_pk)
    except:
        return FileNotFoundError
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        selected_choices = {}
        total_score = calculate_score(request.POST, questions, selected_choices)
        qcount = Question.objects.filter(quiz=quiz).count()
        percentage_score = (total_score / qcount) * 100

        # Now, you can save the selected_choices to the QuizResult
        for question_pk, choice_pk in selected_choices.items():
            question = Question.objects.get(pk=question_pk)
            choice = Choice.objects.get(pk=choice_pk)
            
            quiz_result = QuizResult(
                quiz=quiz,
                user=request.user,
                question=question,  # Set the question here
                selected_choice=choice,  # Set the selected choice here
                score=percentage_score,
            )
            quiz_result.save()

    question_answers = {}
    for question in questions:
        choices = Choice.objects.filter(question=question)
        question_answers[question] = choices
    return render(request, 'active_quiz.html', {'quiz': quiz, 'question_answers': question_answers})




class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


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

