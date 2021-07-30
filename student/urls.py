from django.urls import path
from .import views
from django.contrib.auth.models import User,auth

urlpatterns=[
	path('',views.home,name="home"),
	path('studentdetails',views.studentdetails,name="studentdetails"),
	path('admin',views.admin,name="admin"),
	path('adminhome',views.adminhome,name="adminhome"),
    path('viewdetails',views.viewdetails,name="viewdetails"),

    path("signup/",views.register,name="reg"),
    path("user_login/",views.userlogin,name="user_login"),
    path('accounts/login/login',views.userlogin, name="login"),
    path('accounts/login/userlogin',views.userlogin, name="login"),
    path('accounts/login/userlogin',views.userlogin,name="userlogin"),
    path("signup/login",views.user_login,name="userlogin"),
	
]