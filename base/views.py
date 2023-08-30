from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer  # Import your serializer

@api_view(['GET', 'POST'])
def endpoint(request):
    if request.method == "GET":
        data = Advocate.objects.all()
        serializer = AdvocateSerializer(data, many=True)
        return Response(serializer.data)

          


def advocate_list(request):
    data = ['Dennis','Tada','Max']
    return JsonResponse(data,safe=False)

def advocate_details(request,username):
    data = username
    return JsonResponse(data,safe=False)
