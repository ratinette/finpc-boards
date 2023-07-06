from django.http import HttpResponse

from datetime import datetime
from django.shortcuts import render


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


def example_with_params(request, param):
    return HttpResponse(f"This is an example response with string {param}.")


def example_detail(request, param):
    return HttpResponse(f"This is an example response with id {param}.")
