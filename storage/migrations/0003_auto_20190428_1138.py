# Generated by Django 2.2 on 2019-04-28 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20190428_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='container',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.Container'),
        ),
    ]