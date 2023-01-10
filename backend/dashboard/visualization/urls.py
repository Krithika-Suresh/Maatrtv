from django.urls import path
from . import views

urlpatterns = [
    # path('', views)
    # path('visualization/', views.getDetails),
    # path('visualization/<str:pk>/', views.getDetail),
    # path('', views.HomeView.as_view()),
    # path('visualization/', views.graph),
    path('vitals/', views.VisList.as_view()),
]