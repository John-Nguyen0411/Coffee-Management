# Generated by Django 3.2 on 2022-05-11 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['code']},
        ),
        migrations.RemoveField(
            model_name='ordertable',
            name='table',
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.table'),
        ),
    ]
