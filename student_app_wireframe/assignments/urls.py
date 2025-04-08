from django.urls import path
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('create/', views.assignment_create, name='assignment_create'),
    path('<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('<int:pk>/edit/', views.assignment_update, name='assignment_update'),
    path('<int:pk>/delete/', views.assignment_delete, name='assignment_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),  # Add this line
]