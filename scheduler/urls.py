from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('tasks', TaskListView.as_view(), name='tasks'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/assign/', AssignResourceView.as_view(), name='assign_resource'),
]
