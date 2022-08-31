from django.urls import path
from api import views

urlpatterns = [
    path('stucreate/', views.StudentAPI.as_view()),
    path('stucreate/<int:pk>', views.StudentAPI.as_view()),
]