from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoList.as_view(), name='list'),
    path('create', views.TodoCreate.as_view(), name='create'),
    path('<int:pk>/edit/', views.TodoEdit.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TodoDelete.as_view(), name='delete'),
]
