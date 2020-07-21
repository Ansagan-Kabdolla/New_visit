from django.contrib import admin
from .models import Zakaz

@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ('name','organization','date')
