from django.urls import path
from . import views


urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/<int:pk>/', views.attendance_detail, name='attendance_detail'),
]
