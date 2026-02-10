from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages


def nosotros(request):
    return render(request, "paginas/nosotros.html")


def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        apellido = request.POST.get("apellido", "").strip()
        email_usuario = request.POST.get("email", "").strip()
        telefono = request.POST.get("telefono", "").strip()
        mensaje = request.POST.get("mensaje", "").strip()

        # Validación mínima
        if len(nombre) < 2 or len(apellido) < 2 or "@" not in email_usuario or len(mensaje) < 10:
            messages.error(request, "Revisa los campos antes de enviar.")
            return redirect("contacto")

        asunto = f"Contacto Web — {nombre} {apellido}"
        cuerpo = (
            "Nuevo mensaje desde el formulario de contacto.\n\n"
            f"Nombre: {nombre} {apellido}\n"
            f"Correo del usuario: {email_usuario}\n"
            f"Teléfono: {telefono if telefono else 'No indicado'}\n\n"
            "Mensaje:\n"
            f"{mensaje}\n"
        )

        mail = EmailMessage(
            subject=asunto,
            body=cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,  # web@novamentes.cl
            to=["contacto@novamentes.cl"],
            reply_to=[email_usuario],
        )
        mail.send(fail_silently=False)

        messages.success(request, "¡Gracias! Tu mensaje fue enviado correctamente.")
        return redirect("contacto")

    return render(request, "paginas/contacto.html")
