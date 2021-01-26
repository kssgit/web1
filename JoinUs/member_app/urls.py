from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('signup/', views.signup, name="signup"),
    path('emailCheck/', views.emailCheck, name="emailCheck"),
    path('nicknameCheck/', views.nicknameCheck, name="nicknameCheck"),
    path('memberPage/', views.memberPage, name="memberPage"),
    path('updateNickname/', views.updateNickname, name="updateNickname"),
    path('deleteUser/', views.deleteUser, name="deleteUser"),


]
