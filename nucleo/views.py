from django.shortcuts import render
from django.utils import timezone
from .models import HeroSlide


def home(request):
    now = timezone.now()

    slides = HeroSlide.objects.filter(is_active=True).filter(
        start_at__isnull=True, end_at__isnull=True
    ) | HeroSlide.objects.filter(
        is_active=True, start_at__lte=now, end_at__isnull=True
    ) | HeroSlide.objects.filter(
        is_active=True, start_at__isnull=True, end_at__gte=now
    ) | HeroSlide.objects.filter(
        is_active=True, start_at__lte=now, end_at__gte=now
    )

    slides = slides.distinct().order_by("order", "-created_at")

    return render(request, "nucleo/home.html", {"hero_slides": slides})
