from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('clients/', views.clients),
    path('cars/<int:id>', views.cars),
    path('create-client/', views.create_client),
    path('create-spring/', views.create_spring)
]