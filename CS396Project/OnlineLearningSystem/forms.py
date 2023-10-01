from django import forms
from .models import Post, Reply

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'author', 'body', 'image', 'video')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title your post...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
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

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))
    class Meta:
        model = Reply
        fields = ('content', )

    # content = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'md-textarea form-control',
    #     'placeholder': 'comment here ...',
    #     'rows':'4',
    # }))
    # class Meta: 
    #     model = Reply
    #     fields = ('content',)

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the author here
        form.instance.post = self.post  # Assuming you have a 'post' attribute in your view
        return super().form_valid(form)
    
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.author = self.user  # Assuming you have 'self.user' set in your view
    #     instance.post = self.post  # Assuming you have 'self.post' set in your view
    #     if commit:
    #         instance.save()
    #     return instance