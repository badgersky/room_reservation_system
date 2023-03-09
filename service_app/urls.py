from django.urls import path
from service_app.views import add_room, show_all_rooms, delete_room, modify_room, book_room, show_room_info


urlpatterns = [
    path('room/new/', add_room),
    path('rooms/', show_all_rooms, name='room_list'),
    path('room/delete/<room_id>/', delete_room, name='delete_room'),
    path('room/modify/<room_id>/', modify_room, name='modify_room'),
    path('room/book/<room_id>/', book_room, name='book_room'),
    path('rooms/room/<room_id>/', show_room_info),
]
