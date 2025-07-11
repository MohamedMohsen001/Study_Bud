from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'Lets Learn Python.'},
#     {'id' : 2, 'name' : 'Design with me'},
#     {'id' : 3, 'name' : 'FrontEnd Devs'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def CreateRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)


def UpdateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

def DeleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj' : room})
