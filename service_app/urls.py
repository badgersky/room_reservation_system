from django.urls import path
from service_app.views import add_room


urlpatterns = [
    path('room/new/', add_room)
]
