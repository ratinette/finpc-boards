from django import forms

from app.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "board"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
            "board": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "제목"
        self.fields["content"].label = "내용"
        self.fields["board"].label = "게시판"
        self.fields["board"].empty_label = "게시판 선택"
        self.fields["board"].widget.attrs["class"] = "form-select"

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if not user:
            raise ValueError("User is required")

        instance.author = user

        if commit:
            instance.save()
        return instance
