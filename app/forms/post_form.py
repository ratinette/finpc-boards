from django import forms

from app.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "board"]

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if not user:
            raise ValueError("User is required")

        instance.author = user

        if commit:
            instance.save()
        return instance
