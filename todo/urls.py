from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="list"),
    path("upgrade_task/<str:pk>", views.updateTask, name="upgrade_task"),
    path("delete_task/<str:pk>", views.deleteTask, name="delete_task"),
]