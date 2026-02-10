from django.urls import path
from . import views

urlpatterns = [
    path("", views.cursos_list, name="cursos"),
    path("<slug:slug>/", views.cursos_detail, name="curso_detalle"),
]
