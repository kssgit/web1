from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signupPage, name="signupPage"),
    path('signin/', views.signinPage, name="signinPage"),
    path('noticeboard/', views.noticeboard, name="noticeboard"),
    path('loginCheck/', views.loginCheck, name="loginCheck"),
]
