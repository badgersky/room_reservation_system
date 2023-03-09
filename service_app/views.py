from datetime import datetime, date
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from service_app.models import Room, Reservation
from service_app.utils import modify_room_info, check_date


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
    for room in rooms:
        reservations = [reservation.date for reservation in room.reservation_set.all()]
        room.reserved = date.today() in reservations
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


def book_room(request, room_id):
    if request.method == 'GET':
        reservations = Reservation.objects.filter(room_id=room_id)
        return render(request, 'service_app/book_room.html', {'reservations': reservations})
    elif request.method == 'POST':
        booking_date = request.POST['date']
        booking_date = datetime.strptime(booking_date, '%Y-%m-%d').date()
        if check_date(booking_date):
            return HttpResponse('You have entered date in the past')
        if Reservation.objects.filter(room_id=room_id, date=booking_date).exists():
            return HttpResponse('Reservation for this room, for that day already exists')
        comment = request.POST['comment']
        Reservation.objects.create(room_id=room_id, date=booking_date, comment=comment)
        return redirect('room_list')


def show_room_info(request, room_id):
    if request.method == 'GET':
        room = Room.objects.get(pk=room_id)
        today = date.today()
        future_reservations = Reservation.objects.filter(room_id=room_id, date__gte=today)
        return render(request, 'service_app/show_room_info.html', {
                       'room': room,
                       'reservations': future_reservations
                       })
    elif request.method == 'POST':
        submit = request.POST['button']
        if submit == 'modify':
            return redirect('modify_room', room_id)
        elif submit == 'delete':
            return redirect('delete_room', room_id)
        elif submit == 'book':
            return redirect('book_room', room_id)
