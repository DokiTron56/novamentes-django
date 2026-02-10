from django.db import models
from django.utils.text import slugify

class Curso(models.Model):
    titulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    descripcion_corta = models.CharField(max_length=240)
    contenido = models.TextField()

    imagen = models.ImageField(upload_to="cursos/", blank=True, null=True)

    publicado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)
            slug = base
            n = 1
            while Curso.objects.filter(slug=slug).exists():
                n += 1
                slug = f"{base}-{n}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
