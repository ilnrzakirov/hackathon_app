from django.contrib import admin
from .models import Event, Student, Feedback, Register


# Register your models here.


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ["link"]
    list_display = ("name", "link")
    search_fields = ["name"]
    list_filter = ["type"]


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
