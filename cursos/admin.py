from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "publicado", "created_at")
    list_filter = ("publicado", "created_at")
    search_fields = ("titulo", "descripcion_corta", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}
