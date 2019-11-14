from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quest/', views.quest, name='quest'),
    path('quest2/', views.quest2, name='quest2'),
    path('new/', views.new, name='new'),
    path('add/', views.add, name='add'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('add/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
