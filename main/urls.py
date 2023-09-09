from django.urls import path,include
from .views import *

app_name = "main"

urlpatterns = [
 
    path("login/",login_user ,name="login-user"),
    path("logout/",logout_user ,name="logout-user"),
    
    path("user_details/", user_details ,  name = "details"),
    path("user_details/<str:username>",individual_details ,name="user"),
    # path("post-data/", add_data, name="post-data")
   
    
    

]
