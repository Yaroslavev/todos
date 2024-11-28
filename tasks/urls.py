from django.urls import path
from tasks.views import Home, Details

urlpatterns = [
    path("home/", Home),
    path("details/<int:id>", Details)
]
