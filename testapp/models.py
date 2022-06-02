from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length = 10, primary_key = True)
    number = models.IntegerField()

class Combo(models.Model):
    food = models.ForeignKey(Food, on_delete = models.DO_NOTHING)
    cost = models.IntegerField()


class M0(models.Model):
    m0_id = models.CharField(max_length = 10, primary_key = True)
    data = models.IntegerField()


class M1(models.Model):
    m1_id = models.CharField(max_length = 10, primary_key = True)
    data = models.IntegerField()
    #ManyToManyField
    m1 = models.ManyToManyField(M0, through = 'M3', through_fields = ('m1_a_pk', 'm0_a_pk')) #
    

class M2(models.Model):
    m2_id = models.CharField(max_length = 10, primary_key = True) #, db_column = 'pk_m2'
    m0 = models.ForeignKey(M0, on_delete = models.CASCADE) #, db_column = 'fk_m0'

class M3(models.Model):
    m0_a_pk = models.ForeignKey(M0, on_delete = models.DO_NOTHING)
    m1_a_pk = models.ForeignKey(M1, on_delete = models.DO_NOTHING, related_name = 'a')
    m0_b_pk = models.ForeignKey(M0, on_delete = models.DO_NOTHING, related_name = 'b')
    # m0_b_pk = models.ForeignKey(M0, on_delete = models.DO_NOTHING, related_name = 'b')
    food = models.ForeignKey(Food, on_delete = models.DO_NOTHING)
