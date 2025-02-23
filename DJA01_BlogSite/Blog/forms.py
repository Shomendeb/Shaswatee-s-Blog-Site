from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "post_title",
            "post_content"
        ]  # Add 'category' and 'tag' fields to the form
