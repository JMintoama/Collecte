# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models

class Collecte(models.Model):
    nomrc = models.TextField(primary_key=True)
    n_enregistrement = models.IntegerField()
    datsaisi_c = models.DateField(auto_now_add=True)  # se remplit automatiquement à la création

    def save(self, *args, **kwargs):
        if not self.n_enregistrement:
            last = Collecte.objects.filter(nomrc=self.nomrc).order_by('-n_enregistrement').first()
            self.n_enregistrement = (last.n_enregistrement + 1) if last else 1
        super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'collecte'
# Unable to inspect table 'collecteur'
# The error was: Table collecteur does not exist (empty pragma).


class Indexation(models.Model):
    nomi = models.TextField(primary_key=True)  # The composite primary key (nomi, n_enregistrement) found, that is not supported. The first column is selected.
    n_enregistrement = models.IntegerField()
    dat_reception = models.DateField()
    dat_indexation = models.DateField()
    dat_saisi = models.DateField()
    dat_envoi = models.DateField()

    class Meta:
        managed = False
        db_table = 'indexation'


class Indexeur(models.Model):
    nomi = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'indexeur'
