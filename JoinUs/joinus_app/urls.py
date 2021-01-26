from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.signinPage, name="signinPage"),
    path('logout/', views.logout, name="logout"),
    path('noticeboard/', views.noticeboard, name="noticeboard"),
    path('loginCheck/', views.loginCheck, name="loginCheck"),
]
