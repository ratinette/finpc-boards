from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.models import Board


# Create your views here.


@csrf_exempt
def board_view(request):
    """
    Board 전체 조회 및 생성
    :param request:
    :return:
    """
    if request.method == "GET":
        all_boards = Board.objects.all()
        for board in all_boards:
            print(board.title, board.description)

        try:
            board_by_id = Board.objects.get(id=1)
            print(board_by_id.title, board_by_id.description)
            board_by_pk = Board.objects.get(pk=1)
            print(board_by_pk.title, board_by_pk.description)
        except Board.DoesNotExist:
            print("DoesNotExist")

        board_by_name = Board.objects.filter(title__contains="First").first()

        Board.objects.filter(field__exact="First").last()
        Board.objects.filter(field__exact="First").first()
        Board.objects.filter(field__iexact="First").first()
        Board.objects.filter(field__contains="First").first()
        Board.objects.filter(field__icontains="First").first()
        Board.objects.filter(field__startswith="First").first()
        Board.objects.filter(field__endswith="First").first()
        Board.objects.filter(field__istartswith="First").first()
        Board.objects.filter(field__iendswith="First").first()
        Board.objects.filter(field__in=["First", "Second"]).first()
        Board.objects.filter(field__gt=10).first()
        Board.objects.filter(field__gte=10).first()
        Board.objects.filter(field__lt=10).first()
        Board.objects.filter(field__lte=10).first()
        Board.objects.filter(field__range=(1, 10)).first()
        Board.objects.filter(field__isnull=True).first()

        if board_by_name:
            print(board_by_name.title, board_by_name.description)

        return HttpResponse("GET Func board_view")

    elif request.method == "POST":
        Board.objects.create(title="First Board", description="처음 생성해보는 테이블 입니다.")

        new_board = Board()
        new_board.title = "Second Board"
        new_board.description = "두번째 생성해보는 테이블 입니다."
        new_board.save()

        final_board = Board(title="Third Board", description="세번째 생성해보는 테이블 입니다.")
        final_board.save()
        return HttpResponse("POST Func board_view")
    elif request.method == "PUT":
        board_id = request.GET.get("id")
        try:
            board = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            return HttpResponse("DoesNotExist")
        board.title = "New Title"
        board.save()
        print(board.title, board.description)

        board = Board.objects.filter(id=board_id).update(title="New Title2")
        print(board)  # 1
        return HttpResponse("PUT Func board_view")
    elif request.method == "DELETE":
        board_id = request.GET.get("id")
        try:
            board = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            return HttpResponse("DoesNotExist")
        board.delete()
        return HttpResponse("DEL Func board_view")
    else:
        return HttpResponseNotAllowed(["GET", "POST", "PUT", "DELETE"])


class PostHandler(View):
    def get(self, request, pk):
        return HttpResponse(f"GET Class PostHandler, pk: {pk}")

    def put(self, request, pk):
        return HttpResponse(f"PUT Class PostHandler, pk: {pk}")

    def delete(self, request, pk):
        return HttpResponse(f"DEL Class PostHandler, pk: {pk}")


class PostsHandler(View):
    def get(self, request):
        return HttpResponse(f"GET Class PostsHandler")

    def post(self, request):
        return HttpResponse(f"POST Class PostsHandler")
