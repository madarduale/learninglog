from django.urls import path
from todoapp.views import todoappView, addTodoView, deleteTodoView

urlpatterns = [
    path('todoapp/', todoappView),
     path('addTodoItem/',addTodoView),
     path('deleteTodoItem/<int:i>/', deleteTodoView),
]
