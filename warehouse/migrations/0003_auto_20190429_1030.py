# Generated by Django 2.2 on 2019-04-29 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_warehousecell_barcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
    ]