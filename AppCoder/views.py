from dataclasses import field
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

# Create your views here.

from .models import Paciente, Medico, Turno

# Create your views here.

def inicio (request):
    return render (request, 'AppCoder/padre.html')

class PacienteList(ListView):
    model = Paciente
    template_name = "AppCoder/pacientes_list.html"

class PacienteDetalle(DetailView):
    model = Paciente
    template_name = "AppCoder/paciente_detalle.html"

class PacienteCreacion(CreateView):
    model = Paciente
    success_url = "/AppCoder/paciente/list"
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']

class PacienteUpdate(UpdateView):
    model = Paciente
    success_url = "/AppCoder/paciente/list"
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']

class PacienteDelete(DeleteView):
    model = Paciente
    success_url = "/AppCoder/paciente/list"


class MedicoList(ListView):
    model = Medico
    template_name = "AppCoder/medico_list.html"

class MedicoDetalle(DetailView):
    model = Medico
    template_name = "AppCoder/medico_detalle.html"

class MedicoCreacion(CreateView):
    model = Medico
    success_url = "/AppCoder/medico/list"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class MedicoUpdate(UpdateView):
    model = Medico
    success_url = "/AppCoder/medico/list"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class MedicoDelete(DeleteView):
    model = Medico
    success_url = "/AppCoder/medico/list"

class TurnoList(ListView):
    model = Turno
    template_name = "AppCoder/turno_list.html"

class TurnoDetalle(DetailView):
    model = Turno
    template_name = "AppCoder/turno_detalle.html"

class TurnoCreacion(CreateView):
    model = Turno
    success_url = "/AppCoder/turno/list"
    fields = ['especialidad', 'fecha']

class TurnoUpdate(UpdateView):
    model = Turno
    success_url = "/AppCoder/turno/list"
    fields = ['especialidad', 'fecha']

class TurnoDelete(DeleteView):
    model = Turno
    success_url = "/AppCoder/turno/list"

