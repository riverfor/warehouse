# Generated by Django 2.2 on 2019-05-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0011_auto_20190505_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehousecell',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
