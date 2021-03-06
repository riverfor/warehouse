# Generated by Django 2.2 on 2019-04-30 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20190428_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingmodelproducts',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='base_cont_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ContainerParams', verbose_name='Базовый тип паллеты'),
        ),
        migrations.AlterField(
            model_name='storageunit',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='product.Product', verbose_name='Номенклатура'),
        ),
    ]
