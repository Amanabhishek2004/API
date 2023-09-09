from django.urls import path,include
from . import views


app_name = "base"

urlpatterns = [
    path("advocates/", views.alldata.as_view() , name ="api-data"),

    
    path("advocates/<str:username>", views.endpoint_view , name ="api-data"),
    # path("/", .as_view(), name="")
    path("create-advocate/", views.ModelCreateView.as_view(), name="create"),
    # path("user-data/",views.individual_detail, name = "user-data"),
    path("update-advocates/<str:username>",views.update_advocate, name ="update")
    
]