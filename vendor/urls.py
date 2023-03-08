
from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('profile/', views.vprofile, name='vprofile'),
    path('',AccountViews.vendorDashboard, name='vendor'),

] 
