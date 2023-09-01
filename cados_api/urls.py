
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/", include('base.urls')),
    path("content/", include("main.urls")),
    # path("/", .as_view(), name="")
    # path("content/<str:username>", include("main.urls"))


]
