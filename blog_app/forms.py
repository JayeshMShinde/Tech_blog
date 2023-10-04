from django import forms
from .models import Post  # Import your Post model

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'slug', 'timestamp', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'timestamp':forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'content': forms.Textarea(attrs={'class': 'form-control content-input'}),
        }

        