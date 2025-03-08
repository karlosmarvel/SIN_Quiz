from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Sua URL principal
    path('index/', views.quiz_view, name='quiz_view'),  # Sua URL principal
    path('home/', views.home, name='home'),
]