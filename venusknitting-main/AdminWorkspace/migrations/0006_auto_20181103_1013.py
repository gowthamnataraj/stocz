# Generated by Django 2.1.2 on 2018-11-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminWorkspace', '0005_auto_20181101_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_no',
            field=models.CharField(max_length=50),
        ),
    ]
