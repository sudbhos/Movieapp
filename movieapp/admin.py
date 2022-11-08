from django.contrib import admin
from .models import Movie

class moviein(admin.ModelAdmin):
    list_display = ["rdate","moviename","hero","herine","rating"]

# Register your models here.

admin.site.register(Movie,moviein)
