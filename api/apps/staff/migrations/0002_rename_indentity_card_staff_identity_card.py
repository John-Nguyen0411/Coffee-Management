# Generated by Django 3.2 on 2022-03-31 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='indentity_card',
            new_name='identity_card',
        ),
    ]
