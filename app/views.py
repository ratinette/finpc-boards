from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def example(request):
    # return HttpResponse("This is an example response.")
    return JsonResponse({"message": "This is an example response."})


def example_with_params(request, param):
    return HttpResponse(f"This is an example response with string {param}.")


def example_detail(request, param):
    return HttpResponse(f"This is an example response with id {param}.")
