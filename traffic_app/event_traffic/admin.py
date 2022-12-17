from decouple import config
from django.contrib import admin
from django.utils.html import format_html
from django_object_actions import DjangoObjectActions, action

from .models import Event, Student, Feedback, Register


# Register your models here.


class EventAdmin(DjangoObjectActions, admin.ModelAdmin):
    readonly_fields = ["link"]
    list_display = ("name", "link")
    search_fields = ["name"]
    list_filter = ["type"]
    change_actions = ["action"]
    change_list_template = "custom_admin/change_list.html"
    change_form_template = "custom_admin/change_form.html"

    @action(
        label="This will be the label of the button",
        description="This will be the tooltip of the button"
    )
    def action(self, request, obj):
        pass

    def save_model(self, request, obj, form, change):
        host = config("HOST")
        url = f"{host}event/register_link/{obj.id}"
        obj.link = url
        obj.save()
        return super(EventAdmin, self).save_model(request, obj, form, change)



class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["student", "event", "feedback"]


class RegisterAdmin(admin.ModelAdmin):
    list_display = ["student", "event", "event_check", "link"]


admin.site.register(Event, EventAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Register, RegisterAdmin)
