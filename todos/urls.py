from django.contrib import admin
from django.urls import include, path
import tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include("tasks.urls"))
]
