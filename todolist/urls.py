# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, remove, status, show_json, todolist_ajax, create_task_modal

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('remove/<int:id>', remove, name='remove'),
    path('status/<int:id>', status, name='status'),

    path('todolist_ajax/', show_json, name='show_json'),
    path('json/', todolist_ajax, name='todolist_ajax'),
    path('add/', create_task_modal, name='add'),

]