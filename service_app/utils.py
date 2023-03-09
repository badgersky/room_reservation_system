from service_app.models import Room


def modify_room_info(room, name, capacity, projector):
    room.name = name
    room.seat_number = capacity
    room.projector = projector
    room.save()


def check_date(date):
    today = date.today()
    if today > date:
        return True
    else:
        return False
