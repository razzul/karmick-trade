from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('users', views.user_list, name="user_list"),
]