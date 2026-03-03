from django.urls import path
from . import views

urlpatterns = [
    path('formulario-f12/', views.formulario_f12, name='formulario_f12'),
]