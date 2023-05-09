from django.urls import path

from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserBlogView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.UserBlogPublicView.as_view({'get': 'retrieve'})),
]