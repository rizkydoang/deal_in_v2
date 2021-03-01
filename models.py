# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class TblCategory(models.Model):
    name = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_category'


class TblDataTrans(models.Model):
    deleted = models.CharField(max_length=1)
    id_item = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='id_item')
    id_trans = models.ForeignKey('TblTransaction', models.DO_NOTHING, db_column='id_trans')

    class Meta:
        managed = False
        db_table = 'tbl_data_trans'


class TblDescItem(models.Model):
    description = models.CharField(max_length=300, blank=True, null=True)
    photo = models.CharField(max_length=50)
    price = models.IntegerField()
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_desc_item'


class TblDocuments(models.Model):
    id = models.TextField(primary_key=True)
    photo = models.CharField(max_length=100)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_documents'


class TblItem(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    deleted = models.CharField(max_length=1)
    id_category = models.ForeignKey(TblCategory, models.DO_NOTHING, db_column='id_category')
    id_desc = models.ForeignKey(TblDescItem, models.DO_NOTHING, db_column='id_desc', blank=True, null=True)
    id_store = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_item'


class TblRole(models.Model):
    role = models.CharField(max_length=20)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_role'


class TblStore(models.Model):
    store = models.CharField(primary_key=True, max_length=25)
    deleted = models.CharField(max_length=1)
    username = models.ForeignKey('TblUser', models.DO_NOTHING, db_column='username', blank=True, null=True)
    nik = models.ForeignKey(TblDocuments, models.DO_NOTHING, db_column='nik', blank=True, null=True)
    pin = models.CharField(max_length=4)
    status = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'tbl_store'


class TblTransaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=2)
    total = models.IntegerField()
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_transaction'


class TblUser(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    birth_date = models.DateField()
    deleted = models.CharField(max_length=1)
    id_role = models.ForeignKey(TblRole, models.DO_NOTHING, db_column='id_role')

    class Meta:
        managed = False
        db_table = 'tbl_user'
