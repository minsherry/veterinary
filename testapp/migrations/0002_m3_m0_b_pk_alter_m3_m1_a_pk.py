# Generated by Django 4.0.4 on 2022-06-02 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='m3',
            name='m0_b_pk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='b', to='testapp.m0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='m3',
            name='m1_a_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='a', to='testapp.m1'),
        ),
    ]
