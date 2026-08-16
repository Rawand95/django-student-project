from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]