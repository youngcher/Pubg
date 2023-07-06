from django.urls import path
from pubg import views

urlpatterns = [
    path('', views.index),
    path('create/', views.show_test, name='show_test'),
    path('read/<id>/', views.read),
    path('search/', views.search)
]
