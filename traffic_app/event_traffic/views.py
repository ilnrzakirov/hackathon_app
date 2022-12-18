import qrcode
from decouple import config
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from .forms import RegisterForm, FeedbackForm
from .models import Student, Register, Event, Feedback


def register_to_event(request, pk):
    qr_code = None
    event = None
    profile = None
    if request.method == 'POST':
        login = request.POST["name"]
        email = request.POST["email"]
        host = config("HOST")
        profile = Student.objects.filter(email=email).first()
        if profile:
            use = Register.objects.filter(student=profile, event=Event.objects.get(id=pk)).filter()
            if use:
                return HttpResponse("Уже зарегистрированны")
            event = Register.objects.create(student=profile,
                                            event=Event.objects.get(id=pk),
                                            event_check=False,
                                            link=f"{host}event/check/{profile.id}/{pk}")
            qr_code = qrcode.make(event.link)
        else:
            profile = Student.objects.create(name=login,
                                             email=email)
            event = Register.objects.create(student=profile,
                                            event=Event.objects.get(id=pk),
                                            event_check=False,
                                            link=f"{host}event/check/{profile.id}/{pk}")
            qr_code = qrcode.make(event.link)
        filename = f"{event.event.name}_{profile.name}_{profile.id}.png"
        qr_code.save(filename)
        response = HttpResponse(content_type="image/jpeg")
        image = open(filename, "rb")
        response.content = image
        return response
    else:
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})


def feedback_view(request, pk, event):
    if request.method == 'POST':
        event = Event.objects.get(id=request.POST["event"])
        user = Student.objects.get(id=request.POST["user"])
        feedback = Feedback.objects.create(event=event,
                                           student=user,
                                           feedback=request.POST["feedback"],
                                           description=request.POST["description"])
        return HttpResponse("Спасибо за отзыв")
    else:
        form = FeedbackForm()
        return render(request, "feedback.html", {"form": form, "user": pk, "event": event})


def check_veiw(request, pk, event):
    student = Student.objects.get(id=pk)
    event = Event.objects.get(id=event)
    register = Register.objects.filter(student=student, event=event).first()
    if request.user.is_active:
        register.event_check = True
        register.save()
        return HttpResponse("Ok")
    else:
        return HttpResponse(event)
