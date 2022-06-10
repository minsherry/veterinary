
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class Owner(models.Model):
    '''
    主人
    '''
    first_name = models.CharField(max_length = 12, verbose_name = '名字')
    last_name = models.CharField(max_length = 8, verbose_name = '姓氏')
    phone = models.CharField(max_length = 10, unique = True, verbose_name = '手機號碼')
    birth_date = models.DateField(verbose_name = '生日')
    address = models.CharField(max_length = 80, verbose_name = '地址')
    email = models.EmailField(max_length = 255, verbose_name = '電子信箱')

    @property
    def full_name_zh (self):
        return ("%s%s" %(self.last_name, self.first_name))

    @property
    def full_name_en (self):
        return ("%s %s" %(self.first_name, self.last_name))


class Hospital(models.Model):
    '''
    獸醫院
    '''
    name = models.CharField(max_length = 100, verbose_name = '醫院名')
    phone = models.CharField(max_length = 10, unique = True, verbose_name = '電話號碼')
    address = models.CharField(max_length = 200, verbose_name = '地址')


class Employee(AbstractUser):
    '''
    員工(目前包含醫生.助理)
    '''
    #以下已在 AbstractUser
    # first_name = models.CharField(max_length = 12, verbose_name = '名字')
    # last_name = models.CharField(max_length = 8, verbose_name = '姓氏')
    # email = models.EmailField(max_length = 255, verbose_name = '電子信箱')
    
    phone = models.CharField(blank = True, max_length = 10, unique = True, verbose_name = '手機號碼')
    birth_date = models.DateField(blank = True, verbose_name = '出生年月日')
    address = models.CharField(blank = True, max_length = 80, verbose_name = '地址')
    JOB_CHOICES = [
        (0, '獸醫'),
        (1, '獸醫助理'),
        (2, '寵物美容師'),
        (3, '美容助理'),
    ]
    job = models.IntegerField(choices = JOB_CHOICES, verbose_name = '職別')


class Species(models.Model):
    '''
    寵物種類 非正統
    '''
    SPECIES_ACCEPTABLE = [
        (0, '貓'),
        (1, '狗'),
        (2, '鼠'),
        (3, '鳥'),
        (4, '魚'),
        (5, '貂'),
        (6, '馬'),
        (7, '其他'),
    ]
    species = models.IntegerField(choices = SPECIES_ACCEPTABLE, verbose_name = '種')
    breed = models.CharField(max_length = 50, verbose_name = '品種')



class Pet(models.Model):
    '''
    寵物
    '''
    ID = models.IntegerField(primary_key = True, verbose_name = '晶片號碼', help_text = '晶片號碼是全數字')
    name = models.CharField(max_length = 100, verbose_name = '名字')
    nickname = models.CharField(max_length = 10, verbose_name = '匿稱')
    owner = models.ForeignKey(Owner, on_delete = models.DO_NOTHING, related_name = 'pets', verbose_name = '主人')
    GENDER = [
        (0, 'female'),
        (1, 'male')
    ]
    gender = models.IntegerField(choices = GENDER, verbose_name = '性別')
    birth_date = models.DateField(verbose_name = '出生年月日')
    species = models.ForeignKey(Species, on_delete = models.DO_NOTHING, related_name = 'pets', verbose_name = '品種')


class Reserve(models.Model):
    '''
    預約
    同時可預約多間醫院
    '''
    hospital = models.ForeignKey(Hospital, on_delete = models.DO_NOTHING, related_name = 'reserves', verbose_name = '使用的醫院')
    PURPOSE = [
        (0, '看診'),
        (1, '美容')
    ]
    purpose = models.IntegerField(choices = PURPOSE, verbose_name = '預約目的')
    reserve_datetime = models.DateTimeField(verbose_name = '預約日期、時間', help_text = '依照獸醫/美容師的班來提供可預約時間')
    species = models.ForeignKey(Species, on_delete = models.DO_NOTHING, related_name = 'reserves', verbose_name = '寵物品種')
    detail = models.TextField(verbose_name = '需求')

    class Meta:
        '''
        聯合主鍵
        '''
        unique_together = ('reserve_datetime', 'hospital')


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


class Schedule(models.Model):
    '''
    班表
    如果工作時間有經過24:00
    排班中的休息時間不會另外紀錄
    '''
    work_date = models.DateField(verbose_name = '日期')
    start_work = models.CharField(max_length = 4, verbose_name = '上班幾點幾分', help_text = '前兩位數為幾點 後兩位數為幾分')
    get_off = models.CharField(max_length = 4, verbose_name = '下班幾點幾分', help_text = '前兩位數為幾點 後兩位數為幾分')
    # start_work = models.DateTimeField(verbose_name = '上班時間', help_text = '只記錄幾點幾分,其他年月日都沒有意義')
    # get_off = models.DateTimeField(verbose_name = '下班時間', help_text = '只記錄幾點幾分, 除了隔一天(1/2) 其他年月日都沒有意義')
    # schedule_time = models.ForeignKey(ScheduleTime, on_delete = models.DO_NOTHING, related_name = 'schedules', verbose_name = '上下班時間', help_text = '上班不會超過24Hr')
    employee = models.ForeignKey(Employee, on_delete = models.DO_NOTHING, related_name = 'schedules', verbose_name = '員工')

    @property
    def start_time(self):
        '''
        換算後的時間 主取時間部分
        '''
        return datetime.strptime(self.start_work, '%H%M')

    @property
    def end_time(self):
        '''
        換算後的時間 主取時間部分
        但是如果隔了一天 該datetime 的日期部分會變成 1900-1-2 
        '''
        end = datetime.strptime(self.get_off, '%H%M')

        #判斷是否隔一天
        if self.start_time > end:
            end += timedelta(days = 1)

        return end

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
    assistant = models.ManyToManyField(Employee, verbose_name = '獸醫助理', help_text = '可以同時有多個助理或不用助理')
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
    record_datetime = models.DateTimeField(verbose_name = '美容日期.時間')
    spend_time_in_minute = models.IntegerField(verbose_name = '花費時間(分鐘)')
    pet = models.ForeignKey(Pet, on_delete = models.DO_NOTHING, related_name = 'grooming_recoreds', verbose_name = '寵物')
    groomer = models.ForeignKey(Employee, on_delete = models.DO_NOTHING, related_name = 'groomer_grooming_recoreds', verbose_name = '寵物美容師')
    assistant = models.ManyToManyField(Employee, verbose_name = '美容助理', help_text = '可以同時有多個助理或不用助理')
    gromming_item = models.ManyToManyField(GroomingItem, verbose_name = '美容項目', help_text = '可以同時做多種美容')
    detail = models.TextField(verbose_name = '詳情')