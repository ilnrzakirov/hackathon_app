from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ["link"]
    list_display = ("name", "link")


admin.site.register(Event, EventAdmin)