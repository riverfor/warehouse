# Generated by Django 2.2 on 2019-05-01 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_auto_20190501_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='warehousecell',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
