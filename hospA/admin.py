from django.contrib import admin
from .models import Especialidad, Medico, Paciente

class EspecialidadAdmin(admin.ModelAdmin):
    model = Especialidad
    list_display = ('nombre_esp' , 'descrip')


class MedicoAdmin(admin.ModelAdmin):
    model = Medico
    list_display = ('ident', 'nomb', 'ape', 'num_te', 'dirc',
                    'ciud_resid', 'fecha_naci', 'genero', 'display_espe')
    search_fields = ('nomb', 'ident')

class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    list_display = ('ident', 'nomb', 'ape', 'num_te', 'dirc',
                    'ciud_resid', 'fecha_naci', 'genero')
    search_fields = ('nomb', 'ident')


admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Paciente, PacienteAdmin)