# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    nom = models.TextField()
    email = models.TextField()
    login = models.TextField()
    pass_field = models.TextField(db_column='pass')  # Field renamed because it was a Python reserved word.
    destination = models.TextField()

    class Meta:
        managed = False
        db_table = 'admin'

class Doc(models.Model):
    n_enregistrement = models.AutoField(primary_key=True)
    titre = models.TextField()
    titre_article = models.TextField(blank=True, null=True)
    pages = models.TextField(blank=True, null=True)
    domaine = models.TextField()
    type = models.TextField()
    periodicite = models.TextField(blank=True, null=True)
    vol = models.TextField()
    tom = models.TextField()
    num = models.TextField()
    statut = models.TextField()
    n_periodique = models.IntegerField(blank=True, null=True)
    lang = models.TextField()

    class Meta:
        managed = False
        db_table = 'doc'


class Domaine(models.Model):
    domaine = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'domaine'


class Editeur(models.Model):
    editeur = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'editeur'


class Edition(models.Model):
    editeur = models.TextField() 
    n_enregistrement = models.IntegerField()
    date_edition = models.DateField()
    ville_edition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edition'
        unique_together = ('editeur','n_enregistrement')


class Ecriture(models.Model):
    auteur = models.TextField()  
    n_enregistrement = models.ForeignKey('gestion.Doc', on_delete=models.DO_NOTHING, db_column='n_enregistrement')

    class Meta:
        managed = False
        db_table = 'ecriture'
        unique_together = ('auteur','n_enregistrement')


class Auteur(models.Model):
    auteur = models.TextField()

    class Meta:
        managed = False
        db_table = 'auteur'


class Depot(models.Model):
    type = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'depot'


class Source(models.Model):
    source = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'source'


class Fournit(models.Model):
    source = models.TextField()  
    n_enregistrement = models.IntegerField()
    date_reception = models.DateField()
    obligation = models.TextField()

    class Meta:
        managed = False
        db_table = 'fournit'
        unique_together = ('source','n_enregistrement')

