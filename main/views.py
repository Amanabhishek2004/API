from django.shortcuts import render
from base.models import *
# from django..decorators
import requests
import json
from base.serializers import *
from rest_framework.response import Response
import random
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_details(request):
    n = random.randint(0, 22)
    q = request.GET.get("q" , "") 
    q = str(q)
    response = requests.get(f"http://127.0.0.1:8000/advocates/?q={q}").json()
    
    # print(response.text)

    return render(request, "userpage.html", {"data": response, "n": n})

def individual_details(request, username):
    
    
    # Define data as an empty dictionary initially
    data = {}
    
    # Make the API request to your endpoint
    advocate_data = Advocate.objects.filter(username=username).first()
    form = datacreation(instance = advocate_data)

    if request.method == 'POST':
        form = datacreation(request.POST, instance=advocate_data)
        if form.is_valid():
            form.save()
            data = {
                "Username": form.cleaned_data['username'],
                "company": {
                    "id": form.cleaned_data['company'].id,
                    "name": form.cleaned_data['company'].name,
                    "link": form.cleaned_data['company'].link
                },
                "bio": form.cleaned_data['bio']
            }

            # Make a PATCH request to your API
            response = requests.patch(
                f"http://127.0.0.1:8000/update-advocate/{username}", json=data)

    else:
        # This is not a POST request, you might want to handle other cases here
        form = datacreation(instance=advocate_data)

    api_url = f"http://127.0.0.1:8000/advocates/{username}"
    response = requests.get(api_url).json()
    return render(request, "main.html", {"data": response, "form": form})
    # return render(request, 'main.html', {'form': form})


def delete_data(request, username):

    query = Advocate.objects.get(username=username)
    if request.method == "DELETE":
        query.delete()


def login_user(request):
    

    page = 'login'

    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('you are not a registered user')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:details')
        

    return render(request, 'login.html')

def logout_user(request):
    user = request.user
    logout(request)
    return redirect("main:details")