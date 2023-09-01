from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def endpoint(request):
    if request.method == "GET":
        data = Advocate.objects.all()
        serializer = AdvocateSerializer(data, many=True)
        return Response(serializer.data)





class ModelCreateView(generics.CreateAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer



@api_view(['PATCH'])
def update_advocate(request, username):
    try:
        advocate = Advocate.objects.get(username=username)
    except Advocate.DoesNotExist:
        return Response({"message": "Advocate not found"})

    if request.method == 'PATCH':
        serializer = AdvocateSerializer(advocate, data=request.data, partial=True)  # Use partial=True to allow partial updates

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
# In this example:



# Make sure to replace Advocate with the actual name of your model and AdvocateSerializer with the actual name of your serializer. Additionally, adjust the error handling and response messages as needed for your application.






