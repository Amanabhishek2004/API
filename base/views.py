from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, authentication, permissions
from .models import *
from .serializers import *
from .permissions import *
from django.db.models import Q


class endpoint(generics.RetrieveAPIView, generics.ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    lookup_field = "username"

   


endpoint_view = endpoint.as_view()


class alldata(generics.ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        data = self.request.GET.get("q")
        if data:
            return qs.filter(Q(username__icontains=data) | Q(bio__icontains=data))
        else:
            return qs
        


class ModelCreateView(generics.CreateAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['PATCH'])
def update_advocate(request, username):
    try:
        advocate = Advocate.objects.get(username=username)
    except Advocate.DoesNotExist:
        return Response({"message": "Advocate not found"})

    if request.method == 'PATCH':
        # Use partial=True to allow partial updates
        serializer = AdvocateSerializer(
            advocate, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
# In this example:


# Make sure to replace Advocate with the actual name of your model and AdvocateSerializer with the actual name of your serializer. Additionally, adjust the error handling and response messages as needed for your application.
