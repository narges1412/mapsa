from django.contrib import admin
from django.urls import path
from .views import login_or_register,login_view,register_view,UserEditView,AddCategory,AddToDo,update_todo,ShowAllView




urlpatterns = [
    path('', login_or_register ,name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', UserEditView.as_view(), name='profile'),
    path('Todo/', AddCategory.as_view(), name='Todo'),
    path('ToDo-Add/', AddToDo.as_view(), name='ToDo-Add'),
    path('showall/', ShowAllView.as_view(), name='showall'),
    path('Update-ToDo/<str:pk>', update_todo, name='Update-ToDo'),
]
