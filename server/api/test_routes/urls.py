from django.urls import path
from . import views

urlpatterns = [
    path('nonrest', views.getRoutesNonRestMethod, name='routes'),
    path('rest', views.getRoutesRestMethod, name='routes'),
    path('test/<str:pk>/', views.getSingleRouteRestMethod, name='singleRoute')
]
