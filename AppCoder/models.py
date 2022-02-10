from django.db import models

# Create your models here.
class Turno (models.Model):
    especialidad=models.CharField (max_length=40, null=False) 
    fecha= models.DateField(null=True) 

    def __str__(self):
        return f'El turno en la especialidad: {self.especialidad} tiene fecha: {self.fecha}'

class Paciente (models.Model):
    nombre=models.CharField (max_length=30) 
    apellido= models.CharField (max_length=30)
    email= models.EmailField()
    fecha_nacimiento= models.DateField(null=True)

class Medico (models.Model):
    nombre=models.CharField (max_length=30) 
    apellido= models.CharField (max_length=30)
    email= models.EmailField() 
    profesion= models.CharField (max_length=30)