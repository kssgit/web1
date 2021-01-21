from django.urls import path
from . import views

urlpatterns = [
    path('createPage/', views.createPage, name="createPage"),
    path('meetnameCheck/', views.meetnameCheck, name="meetnameCheck"),
    path('createMeet/', views.createMeet, name="createMeet"),
    path('getMeet/', views.getMeet, name="getMeet"),
    path('updateMeet/', views.updateMeetCheck, name="updateMeetCheck"),




]
