from django.contrib import admin
from django.urls import path, include
from accounts import views  
from django.urls import path
from accounts.views import chatbot_page



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_page, name='welcome_page'),  # Default page
    path('home/', views.home, name='home'),
    path('ai-hiring/', views.ai_hiring, name='ai_hiring'),
    path('learn-more/', views.learn_more, name='learn-more'),
    path('get-started/', views.get_started, name='get-started'),
    path('accounts/', include('accounts.urls')),  # Accounts app ke URLs include karna
    path('chatbot/', include('accounts.urls')),  # This would make final route /chatbot/
    path('chatbot/', chatbot_page, name='chatbot'),
]
