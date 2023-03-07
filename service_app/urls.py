from django.urls import path
from service_app.views import add_room, show_all_rooms, delete_room, modify_room, book_room


urlpatterns = [
    path('room/new/', add_room),
    path('rooms/', show_all_rooms, name='room_list'),
    path('room/delete/<room_id>/', delete_room),
    path('room/modify/<room_id>/', modify_room),
    path('room/book/<room_id>/', book_room),
]
