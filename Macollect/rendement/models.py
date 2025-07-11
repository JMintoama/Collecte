# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Control(models.Model):
    nomc = models.TextField()  
    observation = models.TextField(blank=True, null=True)
    retourne = models.TextField()
    dat_retour = models.DateField(blank=True, null=True)
    dat_valid = models.DateField()
    visa = models.TextField()
    n_enregistrement = models.IntegerField()
    dat_recepc = models.DateField()

    class Meta:
        managed = False
        db_table = 'control'
        unique_together = ('nomc','n_enregistrement')


class Controleur(models.Model):
    nomc = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'controleur'


class Controleurpv(models.Model):
    controleur = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'controleurpv'
