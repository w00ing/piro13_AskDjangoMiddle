from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="list"),
    path("create/", views.create, name="create"),
    path("post/<int:pk>/", views.retrieve, name="retrieve"),
    path("update/<int:pk>/", views.update, name="update"),
    path("post/<int:pk>/delete", views.delete, name="delete"),
]
