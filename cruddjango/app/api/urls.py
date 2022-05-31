from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes, name='student-api'),
    path('students/', views.getStudents, name='student-list'),
    path('students/<str:pk>/', views.getStudent, name='detail'),
    path('create/',views.createStudent, name='create-student'),
    path('update/<str:pk>/',views.updateStudent),
    path('delete/<str:pk>/', views.deleteStudent)
]