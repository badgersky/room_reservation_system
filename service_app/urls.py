from django.urls import path
from service_app.views import add_room, show_all_rooms


urlpatterns = [
    path('room/new/', add_room),
    path('rooms/', show_all_rooms),
]
