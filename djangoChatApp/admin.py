from django.contrib import admin
from .models import Message
from .models import Room

admin.site.register(Message)
admin.site.register(Room)
# Register your models here.
