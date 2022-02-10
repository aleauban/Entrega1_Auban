from dataclasses import field
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Paciente

# Create your views here.

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

class PacienteUpdate(UpdateView):

    model = Paciente
    success_url = "/AppCoder/paciente/list"
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']