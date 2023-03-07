from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from service_app.models import Room
from service_app.utils import modify_room_info


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
                Room.objects.create(name=room_name, seat_number=room_capacity, projector=projector)
                return HttpResponse('Room added')


def show_all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'service_app/show_all_rooms.html', {'rooms': rooms})


def delete_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.delete()
    return redirect('room_list')


def modify_room(request, room_id):
    if request.method == 'GET':
        try:
            room = Room.objects.get(pk=room_id)
        except Room.DoesNotExist:
            return HttpResponse(f'Room with id={room_id} does not exist')
        else:
            return render(request, 'service_app/modify_room.html', {'room': room})
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
            room = Room.objects.get(pk=room_id)
            modify_room_info(room, room_name, room_capacity, projector)
            return redirect('room_list')
