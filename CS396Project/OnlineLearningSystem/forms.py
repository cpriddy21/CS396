from django import forms
from .models import Post

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