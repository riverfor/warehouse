# Generated by Django 2.2 on 2019-05-01 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_auto_20190501_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousecell',
            name='position',
            field=models.CharField(max_length=2, unique=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='warehousecell',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Rack', unique=True, verbose_name='Стеллаж'),
        ),
        migrations.AlterField(
            model_name='warehousecell',
            name='tier',
            field=models.CharField(max_length=2, unique=True, verbose_name='Ярус'),
        ),
    ]
