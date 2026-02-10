from django.contrib import admin
from .models import HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "slide_type", "is_active", "start_at", "end_at", "created_at")
    list_display_links = ("title",)          # ✅ importante
    list_editable = ("order", "is_active")   # ✅ ahora sí se puede
    list_filter = ("is_active", "slide_type")
    search_fields = ("title", "subtitle")
    ordering = ("order", "-created_at")
