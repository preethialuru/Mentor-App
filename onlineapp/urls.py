from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from onlineapp.Views import *
from onlineapp.restapiCollegeView import  *
from onlineapp.restapiStudentView import *

urlpatterns = [
    path('testpath/',my_first_view,name='my_first'),


    path('api/colleges/',api_college_view,name='api_get_college'),
    path('api/colleges/<int:pk>/',api_college_detail_view,name='api_get_college'),
    path('api/colleges/<int:pk>/students/',StudentSerializerView.as_view(),name='api_get_college'),
    path('api/colleges/<int:pk>/students/<int:sk>',StudentSerializerView.as_view(),name='api_get_college'),

    path('colleges/',CollegeView.as_view(),name="colleges_html"),
    path('colleges/<int:pk>',CollegeView.as_view(),name="college_details_id"),
    path('colleges/<str:acronym>',CollegeView.as_view(),name="college_details_acr"),
    #path('colleges/<str:acronym>',CollegeView.as_view(),name="colleges.html"),
    path('colleges/add_college/',AddCollegeView.as_view(),name="add_college"),
    path(r'colleges/<int:pk>/edit',AddCollegeView.as_view(),name="edit_college"),
    path(r'colleges/<int:pk>/delete',AddCollegeView.as_view(),name="delete_college"),
    path('colleges/<int:pk>/add_student',AddStudentView.as_view(),name="add_student"),
    path(r'colleges/<int:pk1>/<int:pk2>/edit',AddStudentView.as_view(),name="edit_student"),
    path(r'colleges/<int:pk1>/<int:pk2>/delete',AddStudentView.as_view(),name="delete_student"),
    path('login/',LoginController.as_view(),name="login"),
    path('signup/',SignUpController.as_view(),name="signup"),
    path('logout/',logout_user,name='logout'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
