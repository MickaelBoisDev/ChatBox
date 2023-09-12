from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Room
from .models import Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        # Vous pouvez ajouter d'autres champs si nécessaire


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Ajustez cette liste pour inclure les champs que vous voulez


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  # Ajustez cette liste pour inclure les champs que vous voulez
