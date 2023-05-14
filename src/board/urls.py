from django.urls import path

from . import views

urlpatterns = [
    path('project/<int:pk>/', views.ProjectView.as_view({"get": "retrieve",
                                                         "put": "update",
                                                         "delete": "destroy"})),
    path('project/', views.ProjectView.as_view({'post': 'create'})),
    path('<int:pk>/', views.ListProjectView.as_view())
]