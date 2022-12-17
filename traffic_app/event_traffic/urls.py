from django.urls import path

from .views import register_to_event, feedback_view

urlpatterns = [
    path('register_link/<int:pk>', register_to_event),
    path('feedback/<int:pk>', feedback_view),
]