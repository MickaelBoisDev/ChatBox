from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Room
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer


def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'list_rooms.html', {'rooms': rooms})


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('list_rooms')
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})


def room_detail(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    messages = room.message_set.all()
    return render(request, 'room_detail.html', {'room': room, 'messages': messages})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)

        # Générer un JWT token pour l'utilisateur
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        user_serializer = UserSerializer(user)

        return Response({"access_token": access_token, "message": "Connexion réussie", "user": user_serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Nom d'utilisateur ou mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)


def logout_view(request):
    logout(request)
    return redirect('login')


@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if password == password2:
        try:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            return Response({"message": "Inscription réussie"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Ce nom d'utilisateur est déjà pris"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Les mots de passe ne correspondent pas"}, status=status.HTTP_400_BAD_REQUEST)
