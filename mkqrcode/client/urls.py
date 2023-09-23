from django.urls import path
from client import views

urlpatterns=[
    path('',views.index,name="index"),
    path("base",views.base,name="base"),
    path("signin",views.signin,name="signin"),
    path("clienthome",views.clienthome,name="clienthome"),
    path("signup",views.signup,name="signup"),
    path('register',views.register,name='register'),
    path("admicheck",views.admicheck,name='admicheck'),
    path("clientlogin",views.clientlogin,name='clientlogin'),
    path("clienthome",views.clienthome,name='clienthome'),
    path("clientdataentry",views.clientdataentry,name='clientdataentry'),
    path("logoutclient",views.logoutclient,name='logoutclient')
]