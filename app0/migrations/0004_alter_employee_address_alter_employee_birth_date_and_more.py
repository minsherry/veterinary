# Generated by Django 4.0.4 on 2022-06-13 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0003_alter_employee_address_alter_employee_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=80, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(verbose_name='出生年月日'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.IntegerField(choices=[(0, '獸醫'), (1, '獸醫助理'), (2, '寵物美容師'), (3, '美容助理')], default='', verbose_name='職別'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='手機號碼'),
            preserve_default=False,
        ),
    ]
