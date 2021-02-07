from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('admin/<str:user>', views.AdminDashboard, name='AdminDashboard'),
    path('assessment/<str:user>', views.Assessment, name='Assessment'),
    path('login', views.LoginUser, name='LoginUser'),
    path('register', views.RegisterUser, name='RegisterUser'),
    path('student_courses/<str:user>', views.StudentCourses, name='StudentCourses'),
    path('report/<str:user>', views.GenerateReport, name='GenerateReport'),
    path('course_assignment/<str:programme>', views.AssignCourses, name='AssignCourses'),
    path('programmes', views.ViewProgrammes, name='ViewProgrammes'),
    path('remove/<str:course>/<str:programme>', views.RemoveCourse, name='RemoveCourse'),
]
