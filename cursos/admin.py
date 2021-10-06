from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Cursos, Aulas

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'descricao')
    search_fields = ('nome', 'descricao')

admin.site.register(Aulas)
