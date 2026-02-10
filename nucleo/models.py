from django.db import models
from django.utils import timezone


class HeroSlide(models.Model):
    class SlideType(models.TextChoices):
        IMAGE_ONLY = "IMAGE_ONLY", "Solo imagen"
        IMAGE_TEXT = "IMAGE_TEXT", "Imagen + texto"

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    slide_type = models.CharField(max_length=20, choices=SlideType.choices, default=SlideType.IMAGE_TEXT)

    # Para “noticias diarias”
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    title = models.CharField(max_length=120, blank=True)
    subtitle = models.CharField(max_length=220, blank=True)

    # Imagen principal del slide (para los 2 tipos)
    image = models.ImageField(upload_to="hero_slides/", null=True, blank=True)

    # Logo opcional (para el tipo imagen + texto)
    logo = models.ImageField(upload_to="hero_slides/logos/", null=True, blank=True)

    cta_text = models.CharField(max_length=40, blank=True)
    cta_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.order} - {self.title or 'Slide'}"

    def is_visible_now(self):
        now = timezone.now()
        if not self.is_active:
            return False
        if self.start_at and now < self.start_at:
            return False
        if self.end_at and now > self.end_at:
            return False
        return True
