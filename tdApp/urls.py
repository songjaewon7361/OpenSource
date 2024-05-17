from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add'),  # Todo 항목 추가 URL
    path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('complete/<int:todo_id>', views.complete_todo, name='complete_todo'),
]
