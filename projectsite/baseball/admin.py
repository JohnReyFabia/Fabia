from django.contrib import admin
from django.contrib.admin import display
from .models import Position


# Register your models here.

@admin.register (Position)
class PositionAdmin (admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)