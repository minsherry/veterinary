# Generated by Django 4.0.4 on 2022-06-01 07:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, verbose_name='名字')),
                ('last_name', models.CharField(max_length=8, verbose_name='姓氏')),
                ('birth_date', models.DateField(verbose_name='生日')),
                ('phone', models.CharField(max_length=10, verbose_name='電話號碼')),
                ('email', models.EmailField(max_length=255, verbose_name='電子信箱')),
                ('address', models.CharField(max_length=80, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, verbose_name='名字')),
                ('last_name', models.CharField(max_length=8, verbose_name='姓氏')),
                ('phone', models.CharField(max_length=10, verbose_name='電話號碼')),
                ('birth_date', models.DateField(verbose_name='生日')),
                ('address', models.CharField(max_length=80, verbose_name='地址')),
                ('email', models.EmailField(max_length=255, verbose_name='電子信箱')),
                ('job', models.IntegerField(choices=[(0, '獸醫'), (1, '獸醫助理'), (2, '寵物美容師'), (3, '美容助理')], verbose_name='職別')),
            ],
        ),
        migrations.CreateModel(
            name='GroomingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='美容項目名稱')),
                ('fee', models.IntegerField(verbose_name='費用')),
                ('symptom', models.TextField(verbose_name='詳情')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='醫院名')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='醫療項目名稱')),
                ('fee', models.IntegerField(verbose_name='費用')),
                ('symptom', models.TextField(verbose_name='詳情')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名字')),
                ('nickname', models.CharField(max_length=10, verbose_name='匿稱')),
                ('gender', models.IntegerField(choices=[(0, 'female'), (1, 'male')], verbose_name='性別')),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='出生年月日')),
                ('species', models.CharField(max_length=100, verbose_name='品種')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pets', to='app0.customer', verbose_name='主人')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_work', models.CharField(help_text='前兩位數為幾點 後兩位數為幾分', max_length=4, verbose_name='上班幾點幾分')),
                ('get_off', models.CharField(help_text='前兩位數為幾點 後兩位數為幾分', max_length=4, verbose_name='下班幾點幾分')),
            ],
            options={
                'unique_together': {('start_work', 'get_off')},
            },
        ),
        migrations.CreateModel(
            name='PetGroomingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_datetime', models.DateTimeField(verbose_name='看診日期.時間')),
                ('spend_time_in_minute', models.IntegerField(verbose_name='花費時間(分鐘)')),
                ('expenditure', models.IntegerField(verbose_name='費用')),
                ('detail', models.TextField(verbose_name='詳情')),
                ('assistant', models.ManyToManyField(help_text='可以同時有多個助理或不用助理', null=True, to='app0.employee', verbose_name='美容助理')),
                ('gromming_item', models.ManyToManyField(help_text='可以同時做多種美容', to='app0.groomingitem', verbose_name='美容項目')),
                ('groomer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='groomer_grooming_recoreds', to='app0.employee', verbose_name='寵物美容師')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='grooming_recoreds', to='app0.pet', verbose_name='寵物')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_datetime', models.DateTimeField(verbose_name='看診日期.時間')),
                ('spend_time_in_minute', models.IntegerField(verbose_name='花費時間(分鐘)')),
                ('detail', models.TextField(verbose_name='詳情')),
                ('assistant', models.ManyToManyField(help_text='可以同時有多個助理或不用助理', null=True, to='app0.employee', verbose_name='獸醫助理')),
                ('medical_item', models.ManyToManyField(help_text='寵物可能同時有多種疾病', to='app0.medicalitem', verbose_name='醫療項目')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mdeical_recoreds', to='app0.pet', verbose_name='寵物')),
                ('veterinary', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='veterinary_mdeical_recoreds', to='app0.employee', verbose_name='獸醫')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.DateField(verbose_name='上班日期')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedules', to='app0.employee', verbose_name='員工')),
                ('schedule_time', models.ForeignKey(help_text='上班不會超過24Hr', on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedules', to='app0.scheduletime', verbose_name='上下班時間')),
            ],
            options={
                'unique_together': {('work_date', 'employee')},
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_datetime', models.DateTimeField(verbose_name='預約日期、時間')),
                ('purpose', models.IntegerField(choices=[(0, '看診'), (1, '美容')], verbose_name='預約目的')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reserves', to='app0.hospital', verbose_name='使用的醫院')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='app0.pet', verbose_name='寵物')),
            ],
            options={
                'unique_together': {('reserve_datetime', 'pet', 'hospital')},
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_date', models.DateField(verbose_name='簽約日期')),
                ('end_date', models.DateField(verbose_name='結束日期')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contracts', to='app0.employee', verbose_name='員工')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contracts', to='app0.hospital', verbose_name='醫院')),
            ],
            options={
                'unique_together': {('sign_date', 'employee')},
            },
        ),
    ]
