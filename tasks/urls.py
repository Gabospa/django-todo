from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('create', views.create , name='create'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete'),
]