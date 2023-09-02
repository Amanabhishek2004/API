from django.urls import path,include
from . import views
urlpatterns = [

    
    path("advocates/<str:username>",views.endpoint_view),
    # path("/", .as_view(), name="")
    path("create-advocate/", views.ModelCreateView.as_view(), name="create"),
    # path("user-data/",views.individual_detail, name = "user-data"),
    path("update-advocates/<str:username>",views.update_advocate, name ="update")
    
]