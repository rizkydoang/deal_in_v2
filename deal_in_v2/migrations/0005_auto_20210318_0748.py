# Generated by Django 3.1.7 on 2021-03-18 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal_in_v2', '0004_auto_20210318_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbldocuments',
            old_name='photo',
            new_name='photo_store',
        ),
    ]