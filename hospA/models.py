from django.db import models

class Especialidad(models.Model):
    nombre_esp = models.CharField(max_length=30, unique=True, blank=False, verbose_name='Nombre Especialidad')
    descrip = models.TextField(verbose_name='Descripción de Especialidad')

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return "%s" % (self.nombre_esp)

class Medico(models.Model):
    ident = models.CharField(max_length=10, unique=True, blank= False, verbose_name='Identificación')
    nomb = models.CharField(max_length=50, verbose_name='Nombre del Médico')
    ape = models.CharField(max_length=50, verbose_name='Apellido del Médico')
    num_te = models.CharField(max_length=10, verbose_name='Numero de Telefono')
    dirc = models.CharField(max_length=100, verbose_name='Dirección')
    ciud_resid = models.CharField(max_length=100, verbose_name='Ciudad de Residencia')
    fecha_naci = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    masc = "Masculino"
    fem = "Femenino"
    gener = [(masc, 'Masculino'), (fem, 'Femenino')]
    genero = models.CharField(max_length=10, choices=gener)
    especialidad = models.ManyToManyField(Especialidad)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __str__(self):
        return "%s %s" % (self.nomb,
                          self.ape)

    def display_espe(self):
        return ', '.join([especialidad.nombre_esp for especialidad in self.especialidad.all()])

    display_espe.short_description = 'Especialidad'

class Paciente(models.Model):
    ident = models.CharField(max_length=10, unique=True, blank= False, verbose_name='Identificación')
    nomb = models.CharField(max_length=50, verbose_name='Nombre del Paciente')
    ape = models.CharField(max_length=50, verbose_name='Apellido del Paciente')
    num_te = models.CharField(max_length=10, verbose_name='Numero de Telefono')
    dirc = models.CharField(max_length=100, verbose_name='Dirección')
    ciud_resid = models.CharField(max_length=100, verbose_name='Ciudad de Residencia')
    fecha_naci = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    masc = "Masculino"
    fem = "Femenino"
    gener = [(masc, 'Masculino'), (fem, 'Femenino')]
    genero = models.CharField(max_length=10, choices=gener)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return "%s %s" % (self.nomb,
                          self.ape)