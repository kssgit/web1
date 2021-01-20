from django.urls import path
from . import views

urlpatterns = [
    path('createPage/', views.createPage, name="createPage"),
    path('meetnameCheck/', views.meetnameCheck, name="meetnameCheck"),
    path('createMeet/', views.createMeet, name="createMeet"),


]
