from django.shortcuts import render, get_object_or_404
from .models import Curso

def cursos_list(request):
    cursos = Curso.objects.filter(publicado=True).order_by("-created_at")
    return render(request, "cursos/cursos_list.html", {"cursos": cursos})

def cursos_detail(request, slug):
    curso = get_object_or_404(Curso, slug=slug, publicado=True)
    return render(request, "cursos/cursos_detail.html", {"curso": curso})
