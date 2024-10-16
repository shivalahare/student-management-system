from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Similar URL patterns for Teacher, Course, Batch, Attendance, Fee...
    path('students/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    # Similar URL patterns for Teacher, Course, Batch, Attendance, Fee...
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/add/', views.teacher_add, name='teacher_add'),
    path('teacher/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teacher/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    # Similar URL patterns for Teacher, Course, Batch, Attendance, Fee...
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/add/', views.course_add, name='course_add'),
    path('course/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),
    # Similar URL patterns for Teacher, Course, Batch, Attendance, Fee...
    path('batches/', views.batch_list, name='batch_list'),
    path('batch/<int:pk>/', views.batch_detail, name='batch_detail'),
    path('batch/add/', views.batch_add, name='batch_add'),
    path('batch/<int:pk>/edit/', views.batch_edit, name='batch_edit'),
    path('batch/<int:pk>/delete/', views.batch_delete, name='batch_delete'),
    # Similar URL patterns for Teacher, Course, Batch, Attendance, Fee...
]
