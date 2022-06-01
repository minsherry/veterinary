from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'birth_date')
admin.site.register(Customer, CustomerAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
admin.site.register(Hospital, HospitalAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('job', 'first_name', 'last_name')
admin.site.register(Employee, EmployeeAdmin)

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'owner', 'species')
admin.site.register(Pet, PetAdmin)

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('reserve_datetime', 'purpose', 'hospital', 'pet')
admin.site.register(Reserve, ReserveAdmin)

class ContractAdmin(admin.ModelAdmin):
    list_display = ( 'employee', 'sign_date', 'hospital', 'end_date')
admin.site.register(Contract, ContractAdmin)

class ScheduleTimeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_work', 'get_off')
admin.site.register(ScheduleTime, ScheduleTimeAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('work_date', 'employee', 'schedule_time')
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