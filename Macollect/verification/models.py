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


class Auteur(models.Model):
    auteur = models.TextField()

    class Meta:
        managed = False
        db_table = 'auteur'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Collecte(models.Model):
    nomrc = models.TextField(primary_key=True)  # The composite primary key (nomrc, n_enregistrement) found, that is not supported. The first column is selected.
    n_enregistrement = models.IntegerField()
    datsaisi_c = models.DateField()

    class Meta:
        managed = False
        db_table = 'collecte'


class Control(models.Model):
    nomc = models.TextField(primary_key=True)  # The composite primary key (nomc, n_enregistrement) found, that is not supported. The first column is selected.
    dat_ctrl = models.DateField()
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


class Depot(models.Model):
    type = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'depot'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Ecriture(models.Model):
    auteur = models.TextField(primary_key=True)  # The composite primary key (auteur, n_enregistrement) found, that is not supported. The first column is selected.
    n_enregistrement = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecriture'


class Editeur(models.Model):
    editeur = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'editeur'


class Edition(models.Model):
    editeur = models.TextField(primary_key=True)  # The composite primary key (editeur, n_enregistrement) found, that is not supported. The first column is selected.
    n_enregistrement = models.IntegerField()
    date_edition = models.DateField()
    ville_edition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edition'


class Fournit(models.Model):
    source = models.TextField(primary_key=True)  # The composite primary key (source, n_enregistrement) found, that is not supported. The first column is selected.
    n_enregistrement = models.IntegerField()
    date_reception = models.DateField()
    obligation = models.TextField()

    class Meta:
        managed = False
        db_table = 'fournit'


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


class Source(models.Model):
    source = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'source'


class Suiveur(models.Model):
    noms = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'suiveur'


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


class Vue(models.Model):
    controleur = models.TextField(primary_key=True)  # The composite primary key (controleur, n_enregistrement) found, that is not supported. The first column is selected.
    n_enregistrement = models.IntegerField()
    dat_ctrl = models.DateField()
    visa = models.TextField()
    dat_recepv = models.DateField()

    class Meta:
        managed = False
        db_table = 'vue'
