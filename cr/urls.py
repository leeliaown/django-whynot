from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_cr/', views.add_cr, name='add-cr'),
    path('update_cr/<int:pk>/<int:task_id>/', views.updateTask, name='update-cr'),
    path('delete_cr/<int:pk>/<int:task_id>/', views.deleteTask, name='delete-cr'),
    path('admin_register/', views.register, name='register'),
    path('engineer_register/', views.engineer_register, name='eng-register'),
    path('search/', views.search_engineer, name='search'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('<int:user_id>/', views.detail, name='detail'),
]