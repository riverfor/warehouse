# Generated by Django 2.2 on 2019-05-04 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20190504_0309'),
        ('incoming', '0012_auto_20190502_0920'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documentproducts',
            unique_together={('document', 'product')},
        ),
    ]
