# Generated by Django 3.2 on 2022-04-18 07:35

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, null=True)),
                ('buying_price', models.DecimalField(decimal_places=0, default=0, max_digits=11, null=True)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'ordering': ('name',), 'verbose_name': 'Equipment', 'verbose_name_plural': 'Equipments'},
        ),
        migrations.AddIndex(
            model_name='equipment',
            index=models.Index(fields=['name'], name='equipments__name_595172_idx'),
        ),
        migrations.AddIndex(
            model_name='material',
            index=models.Index(fields=['name'], name='equipments__name_eed7e0_idx'),
        ),
    ]
