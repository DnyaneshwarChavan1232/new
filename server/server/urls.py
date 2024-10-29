# main_project/urls.py
from django.contrib import admin
from django.urls import path, include
from taskmanagement import views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('taskmanagement.urls')),  # Includes API URLs
    path('', views.home, name='home'),  # Root path for the home view
]
