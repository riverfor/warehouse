# Generated by Django 2.2 on 2019-04-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('warehouse', '0001_initial'),
        ('storage', '0002_auto_20190428_0852'),
        ('product', '0004_auto_20190428_0905'),
        ('incoming', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DocumentEntry',
            new_name='Document_Entry',
        ),
    ]
