from django.shortcuts import render
from base.models import *
# from django..decorators
import requests
import json
from base.serializers import *
from rest_framework.response import Response
import random
from .forms import *
# Create your views here.


def user_details(request):
    n = random.randint(0, 22)
    data = requests.get("http://127.0.0.1:8000/advocates/")
    print(data)
    return render(request, "userpage.html", {"data": data, "n": n})


def individual_details(request, username):

        object = Advocate.objects.get(username=username)
        form = datacreation(instance=object)

        # Make the API request to your endpoint
        api_url = f"http://127.0.0.1:8000/advocates/{username}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON data
            print(data)
            n = random.randint(0, 22)
            return render(request, "main.html", {"data": data, "n": n, "form": form})

        advocate_data = Advocate.objects.filter(username=username).first()

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

    
        return render(request, 'main.html', {'form': form})



def delete_data(request , username):

                query = Advocate.objects.get(username = username)
                if request.method == "DELETE":
                     query.delete()

