from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/',inicio,name="AppCoderInicio"),
    path('paciente/list', PacienteList.as_view(), name='Paciente/List'),
    path('paciente/<int:pk>/', PacienteDetalle.as_view(), name='Paciente/Detail'),
    path('paciente/nuevo/', PacienteCreacion.as_view(), name='Paciente/New'),
    path('paciente/editar/<int:pk>/', PacienteUpdate.as_view(), name='Paciente/Edit'),
    path('paciente/borrar/<int:pk>/', PacienteDelete.as_view(), name='Paciente/Delete'),
    path('medico/list', MedicoList.as_view(), name='Medico/List'),
    path('medico/<int:pk>/', MedicoDetalle.as_view(), name='Medico/Detail'),
    path('medico/nuevo/', MedicoCreacion.as_view(), name='Medico/New'),
    path('medico/editar/<int:pk>/', MedicoUpdate.as_view(), name='Medico/Edit'),
    path('medico/borrar/<int:pk>/', MedicoDelete.as_view(), name='Medico/Delete'),
    path('turno/list', TurnoList.as_view(), name='Turno/List'),
    path('turno/<int:pk>/', TurnoDetalle.as_view(), name='Turno/Detail'),
    path('turno/nuevo/', TurnoCreacion.as_view(), name='Turno/New'),
    path('turno/editar/<int:pk>/', TurnoUpdate.as_view(), name='Turno/Edit'),
    path('turno/borrar/<int:pk>/', TurnoDelete.as_view(), name='Turno/Delete'),
]