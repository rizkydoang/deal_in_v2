# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblCategory(models.Model):
    name = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_category'


class TblDataTrans(models.Model):
    id_item = models.ForeignKey(
        'TblItem', models.DO_NOTHING, db_column='id_item')
    id_trans = models.ForeignKey(
        'TblTransaction', models.DO_NOTHING, db_column='id_trans')
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_data_trans'



class TblItem(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    photo_item = models.ImageField(default='0', upload_to='images/item/')
    price = models.IntegerField(default=0)
    id_store = models.ForeignKey(
        'TblStore', models.DO_NOTHING, db_column='id_store', blank=True, null=True)
    id_category = models.ForeignKey(
        'TblCategory', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_item'


class TblRole(models.Model):
    role = models.CharField(max_length=20)
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_role'


class TblDocuments(models.Model):
    id = models.TextField(primary_key=True)
    photo_store = models.ImageField(upload_to='images/store/')
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_documents'


class TblStore(models.Model):
    status_list = [
        ('0', 'Tunggu Konfirmasi'),
        ('1', 'Aktif'),
        ('2', 'Di Tahan'),
    ]
    id = models.CharField(primary_key=True, max_length=25)
    store = models.CharField(max_length=25, unique=True)
    username = models.ForeignKey(
        'TblUser', models.DO_NOTHING, db_column='username', blank=True, null=True)
    nik = models.ForeignKey(
        'TblDocuments', models.DO_NOTHING, db_column='nik', blank=True, null=True)
    pin = models.CharField(max_length=4)
    status = models.CharField(max_length=2, choices=status_list, default=0)
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_store'


class TblTransaction(models.Model):
    status_list = [
        ('0', 'Belum Transfer'),
        ('1', 'Sedang di kirim'),
        ('2', 'Sukses'),
    ]
    date = models.DateField()
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=2, choices=status_list, default=0)
    total = models.IntegerField()
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_transaction'


class TblUser(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    photo_profile = models.ImageField(default='0', upload_to='images/profile/')
    birth_date = models.DateField()
    id_role = models.ForeignKey(
        'TblRole', models.DO_NOTHING, db_column='id_role')
    deleted = models.CharField(max_length=1, default=0)

    class Meta:
        db_table = 'tbl_user'
