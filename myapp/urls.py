from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario-f01/', views.formulario_f01, name='formulario_f01'),
    path('formulario-f07/', views.formulario_f07, name='formulario_f07'),
    path('formulario-f12/', views.formulario_f12, name='formulario_f12'),
    path('formulario-f42/', views.formulario_f42, name='formulario_f42'),
    path('formulario-f60/', views.formulario_f60, name='formulario_f60'),
]