# Generated by Django 2.2 on 2019-05-01 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20190501_0245'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('vendor', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='storageunit',
            unique_together={('product', 'ratio')},
        ),
    ]
