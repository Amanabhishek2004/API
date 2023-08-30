from django.urls import path,include
from . import views
urlpatterns = [

    path("",views.endpoint , name = "home" ),
    path("advocates/",views.endpoint),
    path("advocates/<str:username>",views.advocate_details)

]