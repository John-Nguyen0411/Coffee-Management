# Generated by Django 3.2 on 2022-04-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_auto_20220418_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
