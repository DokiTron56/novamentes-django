from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    titulo = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField()

    imagen = models.ImageField(upload_to="blog/", blank=True, null=True)

    publicado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)
            slug = base
            n = 1
            while Post.objects.filter(slug=slug).exists():
                n += 1
                slug = f"{base}-{n}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
