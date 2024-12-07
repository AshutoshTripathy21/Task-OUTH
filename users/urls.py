from django.urls import path
from . import views

urlpatterns = [
    path('register/<uidb64>/<token>/', views.user_register, name='user_register'),
]
