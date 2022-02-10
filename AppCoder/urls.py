from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('paciente/list', PacienteList.as_view(), name='List'),
    path('<int:pk>/', PacienteDetalle.as_view(), name='Detail'),
    path('nuevo/', PacienteCreacion.as_view(), name='New'),
    path('editar/<int:pk>/', PacienteUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>/', PacienteDelete.as_view(), name='Delete'),
]