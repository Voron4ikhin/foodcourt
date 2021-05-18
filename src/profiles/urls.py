from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserFCView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.UserFCPublicVIew.as_view({'get': 'retrieve'})),
]