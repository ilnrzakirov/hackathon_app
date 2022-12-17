import qrcode
from decouple import config
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from .models import Student, Register, Event


def register_to_event(request, pk):
    qr_code = None
    event = None
    profile = None
    if request.method == 'POST':
        login = request.POST["login"]
        email = request.POST["email"]
        host = config("HOST")
        profile = Student.objects.filter(email=email).first()
        if profile:
            use = Register.objects.filter(student=profile, event=Event.objects.get(id=pk)).filter()
            if use:
                return HttpResponse("Уже заргеистрированы")
            event = Register.objects.create(student=profile,
                                            event=Event.objects.get(id=pk),
                                            event_check=False,
                                            link=f"{host}event/feedback/{profile.id}")
            qr_code = qrcode.make(event.link)
        else:
            profile = Student.objects.create(name=login,
                                             email=email)
            event = Register.objects.create(student=profile,
                                            event=Event.objects.get(id=pk),
                                            event_check=False,
                                            link=f"{host}event/feedback/{profile.id}")
            qr_code = qrcode.make(event.link)
    filename = f"{event.event.name}_{profile.name}_{profile.id}.png"
    qr_code.save(filename)
    response = HttpResponse(content_type="image/jpeg")
    image = open(filename, "rb")
    response.content = image
    return response


def feedback_view(request, pk):
    return HttpResponse("ok")
