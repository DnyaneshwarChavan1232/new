# taskmanagement/views.py

from rest_framework import viewsets
from django.http import HttpResponse
from .models import Task
from .serializers import TaskSerializer

# API ViewSet for Task model
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Home view with styled welcome message
def home(request):
    html = """
    <html>
        <head>
            <title>Task Management System</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .message-container {
                    text-align: center;
                    border: 2px solid #333;
                    padding: 20px;
                    border-radius: 10px;
                    background-color: #ffffff;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #4CAF50;
                }
                p {
                    font-size: 18px;
                    color: #555;
                }
            </style>
        </head>
        <body>
            <div class="message-container">
                <h1>Welcome to the Task Management System!</h1>
                <p>Your tasks, organized and managed efficiently.</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)
