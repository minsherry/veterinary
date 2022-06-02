from django.contrib import admin
from .models import *

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'number')
admin.site.register(Food, FoodAdmin)

class ComboAdmin(admin.ModelAdmin):
    list_display = ('food', 'cost')
admin.site.register(Combo, ComboAdmin)

admin.site.register(M0)

admin.site.register(M1)

admin.site.register(M2)

admin.site.register(M3)