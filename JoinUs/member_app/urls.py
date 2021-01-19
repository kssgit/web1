from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('signin/', views.signin, name="signin"),
    path('emailCheck/', views.emailCheck, name="emailCheck"),
    path('nicknameCheck/', views.nicknameCheck, name="nicknameCheck"),

]
