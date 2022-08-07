from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


from . import views


urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/',  LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),

    path('', views.TaskList.as_view(), name='tasks'),
    path('task-create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
]
