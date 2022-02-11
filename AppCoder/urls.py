from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('paciente/list', PacienteList.as_view(), name='Paciente/List'),
    path('<int:pk>/paciente', PacienteDetalle.as_view(), name='Detail'),
    path('nuevo/paciente', PacienteCreacion.as_view(), name='New'),
    path('editar/<int:pk>/paciente', PacienteUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>/paciente', PacienteDelete.as_view(), name='Delete'),
    path('medico/list', MedicoList.as_view(), name='Medico/List'),
    path('<int:pk>/medico', MedicoDetalle.as_view(), name='Detail'),
    path('nuevo/medico', MedicoCreacion.as_view(), name='New'),
    path('editar/<int:pk>/medico', MedicoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>/medico', MedicoDelete.as_view(), name='Delete'),
    path('turno/list', TurnoList.as_view(), name='Turno/List'),
    path('<int:pk>/turno', TurnoDetalle.as_view(), name='Detail'),
    path('nuevo/turno', TurnoCreacion.as_view(), name='New'),
    path('editar/<int:pk>/turno', TurnoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>/turno', TurnoDelete.as_view(), name='Delete'),
]