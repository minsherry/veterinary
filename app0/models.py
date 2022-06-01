import datetime

from django.db import models
from tkinter import CASCADE

# Create your models here.


class Customer(models.Model):
    '''
    顧客
    '''
    first_name = models.CharField(max_length = 12, verbose_name = '名字')
    last_name = models.CharField(max_length = 8, verbose_name = '姓氏')
    birth_date = models.DateField(verbose_name = '生日')
    phone = models.CharField(max_length = 10, verbose_name = '電話號碼')
    email = models.EmailField(max_length = 255, verbose_name = '電子信箱')
    address = models.CharField(max_length = 80, verbose_name = '地址')


class Hospital(models.Model):
    '''
    獸醫院
    '''
    name = models.CharField(max_length = 100, verbose_name = '醫院名')
    address = models.CharField(max_length = 200, verbose_name = '地址')


class Employee(models.Model):
    '''
    員工(目前包含醫生.助理)
    '''
    first_name = models.CharField(max_length = 12, verbose_name = '名字')
    last_name = models.CharField(max_length = 8, verbose_name = '姓氏')
    phone = models.CharField(max_length = 10, verbose_name = '電話號碼')
    birth_date = models.DateField(verbose_name = '生日')
    address = models.CharField(max_length = 80, verbose_name = '地址')
    email = models.EmailField(max_length = 255, verbose_name = '電子信箱')
    JOB_CHOICES = [
        (0, '獸醫'),
        (1, '獸醫助理'),
        (2, '寵物美容師'),
        (3, '美容助理'),
    ]
    job = models.IntegerField(choices = JOB_CHOICES, verbose_name = '職別')


class Pet(models.Model):
    '''
    寵物
    '''
    name = models.CharField(max_length = 200, verbose_name = '名字')
    nickname = models.CharField(max_length = 10, verbose_name = '匿稱')
    owner = models.ForeignKey(Customer, on_delete = models.DO_NOTHING, related_name = 'pets', verbose_name = '主人')
    GENDER = [
        (0, 'female'),
        (1, 'male')
    ]
    gender = models.IntegerField(choices = GENDER, verbose_name = '性別')
    birth_date = models.DateField(default = datetime.date.today, verbose_name = '出生年月日')
    species = models.CharField(max_length = 100, verbose_name = '品種')


class Reserve(models.Model):
    '''
    預約
    同時可預約多間醫院
    '''
    reserve_datetime = models.DateTimeField(verbose_name = '預約日期、時間')
    pet = models.ForeignKey(Pet, on_delete = models.CASCADE, related_name = 'reserves', verbose_name = '寵物')
    PURPOSE = [
        (0, '看診'),
        (1, '美容')
    ]
    purpose = models.IntegerField(choices = PURPOSE, verbose_name = '預約目的')
    hospital = models.ForeignKey(Hospital, on_delete = models.DO_NOTHING, related_name = 'reserves', verbose_name = '使用的醫院')

    class Meta:
        '''
        聯合主鍵
        '''
        unique_together = ('reserve_datetime', 'pet', 'hospital')


class Contract(models.Model):
    '''
    醫院與員工的合約
    '''
    sign_date = models.DateField(verbose_name = '簽約日期')
    end_date = models.DateField(verbose_name = '結束日期')
    hospital = models.ForeignKey(Hospital, on_delete = models.DO_NOTHING, related_name = 'contracts', verbose_name = '醫院')
    employee = models.ForeignKey(Employee, on_delete = models.DO_NOTHING, related_name = 'contracts', verbose_name = '員工')

    class Meta:
        '''
        聯合主鍵
        '''
        unique_together = ('sign_date', 'employee')


class ScheduleTime(models.Model):
    '''
    上班時間
    預設不會工作超過24小時
    被
    '''
    start_work = models.CharField(max_length = 4, verbose_name = '上班幾點幾分', help_text = '前兩位數為幾點 後兩位數為幾分')
    get_off = models.CharField(max_length = 4, verbose_name = '下班幾點幾分', help_text = '前兩位數為幾點 後兩位數為幾分')

    class Meta:
        '''
        聯合主鍵
        '''
        unique_together = ('start_work', 'get_off')
    
    #可以用 @property 來建立一個唯獨的def來讀取工作時間
    # @property
    # def get_work_time(self):
    #     '''
    #     工作時數
    #     '''
    #     if self.get_off > self.start_work:
    #         return self.get_off - self.start_work
    #     if self.get_off == self.start_work:
    #         return 24
    #     else:
    #         return 24 - self.get_off - self.start_work


class Schedule(models.Model):
    '''
    班表
    '''
    work_date = models.DateField(verbose_name = '上班日期')
    # TYPE = [
    #     (0, '早班'),
    #     (1, '晚班')
    # ]
    # schedule_time = models.IntegerField(choices = TYPE, verbose_name = '班別')
    schedule_time = models.ForeignKey(ScheduleTime, on_delete = models.DO_NOTHING, related_name = 'schedules', verbose_name = '上下班時間', help_text = '上班不會超過24Hr')
    employee = models.ForeignKey(Employee, on_delete = models.DO_NOTHING, related_name = 'schedules', verbose_name = '員工')

    class Meta:
        '''
        聯合主鍵
        '''
        unique_together = ('work_date', 'employee')


class MedicalItem(models.Model):
    '''
    醫療項目 可以是疾病、受傷 等
    '''
    name = models.CharField(max_length = 100, verbose_name = '醫療項目名稱')
    fee = models.IntegerField(verbose_name = '費用')
    symptom = models.TextField(verbose_name = '詳情')


class MedicalRecord(models.Model):
    '''
    寵物看診紀錄
    '''
    record_datetime = models.DateTimeField(verbose_name = '看診日期.時間')
    spend_time_in_minute = models.IntegerField(verbose_name = '花費時間(分鐘)')
    pet = models.ForeignKey(Pet, on_delete = models.DO_NOTHING, related_name = 'mdeical_recoreds', verbose_name = '寵物')
    veterinary = models.ForeignKey(Employee, on_delete = models.DO_NOTHING, related_name = 'veterinary_mdeical_recoreds', verbose_name = '獸醫')
    assistant = models.ManyToManyField(Employee, null = True, verbose_name = '獸醫助理', help_text = '可以同時有多個助理或不用助理')
    medical_item = models.ManyToManyField(MedicalItem, verbose_name = '醫療項目', help_text = '寵物可能同時有多種疾病')
    detail = models.TextField(verbose_name = '詳情')


class GroomingItem(models.Model):
    '''
    美容項目 修毛
    '''
    name = models.CharField(max_length = 100, verbose_name = '美容項目名稱')
    fee = models.IntegerField(verbose_name = '費用')
    symptom = models.TextField(verbose_name = '詳情')


class PetGroomingRecord(models.Model):
    '''
    寵物美容紀錄
    '''
    record_datetime = models.DateTimeField(verbose_name = '看診日期.時間')
    spend_time_in_minute = models.IntegerField(verbose_name = '花費時間(分鐘)')
    pet = models.ForeignKey(Pet, on_delete = models.DO_NOTHING, related_name = 'grooming_recoreds', verbose_name = '寵物')
    groomer = models.ForeignKey(Employee, on_delete = models.DO_NOTHING, related_name = 'groomer_grooming_recoreds', verbose_name = '寵物美容師')
    assistant = models.ManyToManyField(Employee, null = True, verbose_name = '美容助理', help_text = '可以同時有多個助理或不用助理')
    gromming_item = models.ManyToManyField(GroomingItem, verbose_name = '美容項目', help_text = '可以同時做多種美容')
    detail = models.TextField(verbose_name = '詳情')