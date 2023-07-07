from django.urls import path
from pubg import views


urlpatterns = [
    path('', views.index),
    path('show_test/', views.show_test, name='show_test'),
    path('read/<id>/', views.read),
    path('search/', views.search)
]
