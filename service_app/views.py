from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from service_app.models import Room


def add_room(request):
    if request.method == 'GET':
        return render(request, 'service_app/add_room.html')
    elif request.method == 'POST':
        try:
            room_name = request.POST['name']
            room_capacity = int(request.POST['seats_num'])
            projector = request.POST.get('projector', False)
        except MultiValueDictKeyError:
            return HttpResponse('Invalid input data')
        else:
            if projector == 'True':
                projector = True
            if Room.objects.filter(name=room_name).exists():
                return HttpResponse('Room already exists')
            else:
                Room.objects.create(
                    name=room_name,
                    seat_number=room_capacity,
                    projector=projector
                    )
                return HttpResponse('Room created')
