from django.urls import path

from .views import register_to_event

urlpatterns = [
    path('register_link/<int:pk>', register_to_event),
]