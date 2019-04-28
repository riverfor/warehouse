# Generated by Django 2.2 on 2019-04-28 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('warehouse', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.WarehouseCell', verbose_name='Ячейка')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Container')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_storage.storage_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ContainerProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Срок годности')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Container')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Номенклатура')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.StorageUnit', verbose_name='Единица хранения')),
            ],
        ),
    ]
