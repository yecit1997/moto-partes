from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.crear_producto),
]
