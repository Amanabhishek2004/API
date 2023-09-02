from django.urls import path,include
from .views import *


urlpatterns = [
 

    path("user_details/", user_details),
    path("user_details/<str:username>",individual_details ,name="user"),
    # path("post-data/", add_data, name="post-data")
   
    
    

]
