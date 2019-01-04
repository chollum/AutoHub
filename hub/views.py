from django.shortcuts import render
import requests
from .models import Room
# Create your views here.
def data(request):
    rooms = Room.objects.all()

    room_data = []
    for room in rooms:
        data = {
            'id': room.id,
            'tag': room.tag,
            'temperature': room.temperature,
            'humidity': room.humidity,
            'description': room.description
        }
        room_data.append(data)
    context = {'room_data':room_data}
    return render(request, 'hub/data.html', context)

def doors(request):
    return render(request, 'hub/doors.html')

def lights(request):
    return render(request, 'hub/lights.html')

def test(request):
    return render(request, 'hub/test.html')

def chat(request):
    return render(request, 'hub/chat.html')
