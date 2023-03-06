from django.urls import path
from service_app.views import add_room, show_all_rooms, delete_room


urlpatterns = [
    path('room/new/', add_room),
    path('rooms/', show_all_rooms, name='room_list'),
    path('room/delete/<room_id>/', delete_room),
]
