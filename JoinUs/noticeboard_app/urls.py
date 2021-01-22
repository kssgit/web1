from django.urls import path
from . import views

urlpatterns = [
    path('createPage/', views.createPage, name="createPage"),
    path('meetnameCheck/', views.meetnameCheck, name="meetnameCheck"),
    path('updatemeetnameCheck/', views.updatemeetnameCheck,
         name="updatemeetnameCheck"),
    path('createMeet/', views.createMeet, name="createMeet"),
    path('getMeet/', views.getMeet, name="getMeet"),
    path('updateMeetCheck/', views.updateMeetCheck, name="updateMeetCheck"),
    path('update/', views.updateMeet, name="updateMeet"),
    path('deleteMeet/', views.deleteMeet, name="deleteMeet"),
    path('joinMeet/', views.joinMeet, name="joinMeet"),


]
