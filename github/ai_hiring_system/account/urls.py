from django.urls import path
from . import views  
from django.shortcuts import render# Pura views module import karo
from .views import chatbot_response
from .views import chatbot_page, chatbot_response  # Ensure correct import

urlpatterns = [
    path('', views.home, name='home'),  # Default Home
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post-job/', views.post_job, name='post_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),  # Job Detail
    path('job-recommendations/', views.job_recommendations, name='job_recommendations'),
    path('find-expert/', views.find_expert, name='find_expert'),
    path('search-experts/', views.search_experts, name='search_experts'),
    path('experts/', views.experts_page, name='experts'),
    path('apply/', views.apply_for_job, name='apply_for_job'),  # Job Apply Page
    path("learn-more/", lambda request: render(request, "accounts/learn-more.html"), name="learn_more"),
     path('get-started/', views.get_started, name='get-started'),
    path('get-started/services/', views.services, name='services'),
     # Frontend page
   path("chatbot-response/", chatbot_response, name="chatbot_response"),

]

