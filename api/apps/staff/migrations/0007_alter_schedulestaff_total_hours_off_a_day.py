# Generated by Django 3.2 on 2022-04-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_schedulestaff_total_hours_off_a_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulestaff',
            name='total_hours_off_a_day',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]