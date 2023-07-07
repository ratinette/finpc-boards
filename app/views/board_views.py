from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.forms.post_form import CreatePostForm
from app.models import Board, Post


def index(request):
    rendering_info = dict(
        title="Home",
        user_id=1,
        date_joined=datetime(2022, 1, 1, 0, 0, 0),
        category_list=[1, 2, 3],
        price=1000,
        note=None,
        msg="Hello World",
        java="Java",
        python="Python",
    )

    return render(request, "index.html", rendering_info)


@csrf_exempt
def board_view(request):
    """
    Board 전체 조회 및 생성
    :param request:
    :return:
    """
    if request.method == "GET":
        board_id = request.GET.get("id")
        posts = []

        board_list = Board.objects.all()

        if board_id:
            posts = Post.objects.filter(board_id=board_id).order_by("-id").all()

        return render(request, "board.html", {"board_list": board_list, "posts": posts})


class PostHandler(View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            post = None
        return render(request, "post.html", {"post": post})


class PostsHandler(View):
    def get(self, request):
        form = CreatePostForm()
        return render(request, "create_post.html", {"form": form})

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            saved_form = form.save(user=request.user)
            return redirect("post", pk=saved_form.id)
        return render(request, "create_post.html", {"form": form})


def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("post", pk=pk)
    else:
        form = CreatePostForm(instance=post)

    return render(request, "create_post.html", {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    post.delete()
    return redirect("boards")
