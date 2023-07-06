from django.urls import path
from pubg import views

urlpatterns = [
    path('', views.index),
    path('create/', views.index),
    path('read/1/', views.index)
]
