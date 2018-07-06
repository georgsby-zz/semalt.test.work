from django.urls import path
from web.views import HomeView, TaskSolveView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('task/<int:pk>/', TaskSolveView.as_view(), name='task'),
]
