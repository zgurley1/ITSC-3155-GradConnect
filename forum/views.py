from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Message, Profile

def login_view(request):
    return render(request, 'forum/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'forum/signup.html', {'form': form})

def main_page(request):
    rooms = Room.objects.all()  # Fetch popular rooms
    return render(request, 'forum/main_page.html', {'rooms': rooms})

def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        topic = request.POST.get('topic')
        description = request.POST.get('description')
        room = Room.objects.create(name=name, topic=topic, description=description, creator=request.user)
        return redirect('room_detail', room_id=room.id)
    return render(request, 'forum/create_room.html')

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    messages = Message.objects.filter(room=room)
    return render(request, 'forum/room_detail.html', {'room': room, 'messages': messages})

def direct_messages(request):
    messages = Message.objects.filter(sender=request.user)  # Fetch user's messages
    return render(request, 'forum/direct_messages.html', {'messages': messages})

def profile_view(request, username):
    user_profile = Profile.objects.get(user__username=username)
    return render(request, 'forum/profile.html', {'profile': user_profile})
