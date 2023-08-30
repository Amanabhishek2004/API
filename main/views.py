from django.shortcuts import render
import requests
import json



# Create your views here.
def user_details(request):
    
    data = requests.get("http://127.0.0.1:8000/advocates").json()
    print(data)
    return render(request , "main.html",{"data":data})
