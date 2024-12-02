from django.urls import path
from tasks.views import Delete, Home, Details, Create

urlpatterns = [
    path("", Home, name = 'home'),
    path("details/<int:id>", Details, name = 'details'),
    path("create/", Create, name = 'create'),
    path("delete/<int:id>", Delete, name = 'delete')
]
