# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models

class Collecteur(models.Model):
    nomrc = models.TextField(primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'Collecteur'

class Collecte(models.Model):
    id = models.AutoField(primary_key=True)
    nomrc = models.CharField(max_length=255)
    n_enregistrement = models.IntegerField()
    datsaisi_c = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'collecte'
        unique_together = ('nomrc','n_enregistrement')

class Indexation(models.Model):
    id = models.AutoField(primary_key=True)
    nomi = models.TextField()  
    n_enregistrement = models.IntegerField()
    dat_reception = models.DateField()
    dat_indexation = models.DateField()
    dat_saisi = models.DateField()
    dat_envoi = models.DateField()

    class Meta:
        managed = False
        db_table = 'indexation'
        unique_together = ('nomi','n_enregistrement')


class Indexeur(models.Model):
    nomi = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'indexeur'
