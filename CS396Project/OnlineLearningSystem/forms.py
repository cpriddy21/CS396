from django import forms
from .models import Post, Reply, QuizResult, Choice

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'body', 'image', 'video')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title your post...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your post...'}),
            
            
        }

class UpdatePostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'body','image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title your post...'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your post...'}),
            
        }


class ReplyForm(forms.ModelForm):

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))
    class Meta:
        model = Reply
        fields = ('body', )

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the author here
        form.instance.post = self.post  # Assuming you have a 'post' attribute in your view
        return super().form_valid(form)
    
class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = QuizResult
        fields = ['selected_choice'] 
    selected_choice = forms.ModelChoiceField(
        queryset=Choice.objects.all(),
        required=True,  # Set to True if it should be required
        widget=forms.RadioSelect,
    )
   