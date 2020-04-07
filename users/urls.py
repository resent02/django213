from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns =[

    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('students/account-student/teachers-list', MentorListView.as_view(), name='teachers_list'),
    path('students/account-student/', StudentProfileView.as_view(), name='student_profile'),
    path('mentors/account-mentor/subscribers-list', subscribers_list, name='my_subscribers'),
    path('mentors/account-mentor/', MentorProfileView.as_view(), name='mentor_profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('course/add/', CourseCreateView.as_view(), name='course_add'),
    path('course/<int:pk>/detail', CourseDetail.as_view(), name='course_detail'),
    path('course/<int:pk>/update', CourseUpdateView.as_view(), name='course_change'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('reg-student', StudentSignUpView.as_view(), name='reg-student'),
    path('reg-mentor', MentorSignUpView.as_view(), name='reg-mentor'),
    path('courses_list/', CourseListView.as_view(), name='courses_list'),
    path('mentor_profile/<int:pk>/', MentorProfile.as_view(), name='mentor_detail'),
    path('course_detail/<int:pk>/like/', CourseLike.as_view(), name='course_like'),
]
