# Generated by Django 2.1.2 on 2018-10-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaffWorkspace', '0004_report_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='ending_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='previous_balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='purchase',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]