from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "publicado", "created_at")
    list_filter = ("publicado", "created_at")
    search_fields = ("titulo", "resumen", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}
