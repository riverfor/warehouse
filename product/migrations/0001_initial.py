# Generated by Django 2.2 on 2019-04-28 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingModelProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('use_date', models.BooleanField(default=False, verbose_name='Учет по срока годности')),
                ('use_serial', models.BooleanField(default=False, verbose_name='Учет по серийным номерам')),
                ('use_parts', models.BooleanField(default=False, verbose_name='Учет по партиям')),
            ],
            options={
                'verbose_name': 'Модель учета',
                'verbose_name_plural': 'Модели учета',
            },
        ),
        migrations.CreateModel(
            name='ContainerParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cont_width', models.IntegerField(verbose_name='Ширина')),
                ('cont_height', models.IntegerField(verbose_name='Высота')),
                ('cont_length', models.IntegerField(verbose_name='Глубина')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=20)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('base_cont_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ContainerParams')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.AccountingModelProducts', verbose_name='Модель учета')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Номенклатуры',
            },
        ),
        migrations.CreateModel(
            name='StorageUnitsClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Класс единица хранения',
                'verbose_name_plural': 'Классы единиц хранения',
            },
        ),
        migrations.CreateModel(
            name='StorageUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.IntegerField(default=1, verbose_name='коэфициент')),
                ('unit_width', models.DecimalField(decimal_places=3, max_digits=5, max_length=10, verbose_name='Ширина')),
                ('unit_height', models.DecimalField(decimal_places=3, max_digits=5, max_length=10, verbose_name='Высота')),
                ('unit_length', models.DecimalField(decimal_places=3, max_digits=5, max_length=10, verbose_name='Глубина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Номенклатура')),
                ('unit_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.StorageUnitsClass', verbose_name='Класс единицы хранения')),
            ],
            options={
                'verbose_name': 'Единица хранения',
                'verbose_name_plural': 'Единицы хранения',
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=20, unique=True)),
                ('cont_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ContainerParams')),
            ],
        ),
    ]
