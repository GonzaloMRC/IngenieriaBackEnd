from django.urls import path
from . import views
from ..api import simulate

urlpatterns = [
    path('', views.hello1),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('clients/', views.clients),
    path('cars/<int:id>', views.cars),
    path('create-client/', views.create_client),
    path('create-spring/', views.create_spring),
    path('simulate-spring/', views.simulate_spring)
]