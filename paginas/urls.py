from django.urls import path
from .views import contacto

urlpatterns = [
    path("contactanos/", contacto, name="contacto"),
]
