from decouple import config
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import admin
from django.core.mail import send_mail
from django.utils.html import format_html
from django_object_actions import DjangoObjectActions, action, takes_instance_or_queryset

from .models import Event, Student, Feedback, Register


# Register your models here.


class EventAdmin(DjangoObjectActions, admin.ModelAdmin):
    readonly_fields = ["link"]
    list_display = ("name", "link")
    search_fields = ["name"]
    list_filter = ["type"]
    change_actions = ["action"]
    changelist_actions = ["get_feedback"]
    actions = ["get_feedback"]
    change_list_template = "custom_admin/change_list.html"
    change_form_template = "custom_admin/change_form.html"

    @action(
        label="This will be the label of the button",
        description="This will be the tooltip of the button"
    )
    def action(self, request, obj):
        pass

    @takes_instance_or_queryset
    def get_feedback(self, request, queryset):
        host = config("HOST")
        for event in queryset:
            students = Register.objects.filter(event=event)
            for student in students:
                feedback_link = f"{host}event/feedback/{student.student.id}/{student.event.id}"
                send_mail("Оставьте отзыв о мероприятии",
                          f"Ссылка для отзыва: {feedback_link}",
                          EMAIL_HOST_USER,
                          [student.student.email, ])
                print(feedback_link)

    get_feedback.label = "Попросить отзыв"
    get_feedback.short_descriptions = "Попросить отзыв"

    def save_model(self, request, obj, form, change):
        obj.save()
        host = config("HOST")
        url = f"{host}event/register_link/{obj.id}"
        obj.link = url
        obj.save()
        return super(EventAdmin, self).save_model(request, obj, form, change)


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["student", "event", "feedback", "description"]
    list_filter = ["event", "feedback"]
    search_fields = ["student", "event"]


class RegisterAdmin(admin.ModelAdmin):
    list_display = ["student", "event", "event_check", "link"]
    list_filter = ["event"]
    search_fields = ["student", "event"]


admin.site.site_header = "Администриарование мероприятий"
admin.site.register(Event, EventAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Register, RegisterAdmin)