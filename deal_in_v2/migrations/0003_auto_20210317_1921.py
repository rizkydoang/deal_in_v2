# Generated by Django 3.1.7 on 2021-03-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_in_v2', '0002_auto_20210301_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbldocuments',
            name='photo',
            field=models.ImageField(upload_to='images/profile/'),
        ),
    ]
