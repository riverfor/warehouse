# Generated by Django 2.2 on 2019-04-29 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incoming', '0005_auto_20190429_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentproducts',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='incoming.DocumentPlan'),
        ),
    ]
