# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Suivi(models.Model):
    noms = models.TextField()
    n_enregistrement = models.IntegerField()
    datenvoi_t = models.DateField()
    dat_rsuivi = models.DateField()
    datsaisi_ic = models.DateField()
    datenvoi_sir = models.DateField()
    dat_pv = models.DateField()
    dat_mont = models.DateField()
    dat_rrsuivi = models.DateField()
    datsaisi_pv = models.DateField()

    class Meta:
        managed = False
        db_table = 'suivi'


class Suiveur(models.Model):
    noms = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'suiveur'


class Vue(models.Model):
    controleur = models.TextField()  
    n_enregistrement = models.IntegerField()
    dat_ctrl = models.DateField()
    visa = models.TextField()
    dat_recepv = models.DateField()

    class Meta:
        managed = False
        db_table = 'vue'
        unique_together = ('controleur','n_enregistrement')
