from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["GET"])
def endpoint(request):
    data = ["/advocates", "advocates/:username"]
    return JsonResponse(data = data,safe=False)


def advocate_list(request):
    data = ['Dennis','Tada','Max']
    return JsonResponse(data,safe=False)

def advocate_details(request,username):
    data = username
    return JsonResponse(data,safe=False)
