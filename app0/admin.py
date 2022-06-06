from django.contrib import admin
from .models import *

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'birth_date')
admin.site.register(Owner, OwnerAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
admin.site.register(Hospital, HospitalAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('job', 'first_name', 'last_name')
admin.site.register(Employee, EmployeeAdmin)

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('species', 'breed')
admin.site.register(Species, SpeciesAdmin)

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'owner', 'species')
admin.site.register(Pet, PetAdmin)

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'reserve_datetime', 'purpose', 'species')
admin.site.register(Reserve, ReserveAdmin)

class ContractAdmin(admin.ModelAdmin):
    list_display = ( 'employee', 'sign_date', 'hospital', 'end_date')
admin.site.register(Contract, ContractAdmin)

# class ScheduleTimeAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'start_work', 'get_off')
# admin.site.register(ScheduleTime, ScheduleTimeAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('work_date', 'employee', 'start_work', 'get_off')
admin.site.register(Schedule, ScheduleAdmin)

class MedicalItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'fee', 'symptom')
admin.site.register(MedicalItem, MedicalItemAdmin)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'record_datetime', 'veterinary', 'pet')
admin.site.register(MedicalRecord, MedicalRecordAdmin)

class GroomingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'fee', 'symptom')
admin.site.register(GroomingItem, GroomingItemAdmin)

class PetGroomingRecordAdmin(admin.ModelAdmin):
    list_display = ('record_datetime', 'groomer', 'pet')
admin.site.register(PetGroomingRecord, PetGroomingRecordAdmin)