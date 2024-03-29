from django.urls import path 
from . import views

app_name = 'board'

urlpatterns = [
    # board/create/
    path('create/', views.create, name='create'),
    # board/
    path('', views.index, name='index'),
    # board/1/
    path('<int:pk>/', views.detail,name='detail'),
    # board/1/update/
    path('<int:pk>/update/', views.update, name='update'),
    # board/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
]
