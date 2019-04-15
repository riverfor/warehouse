# Generated by Django 2.2 on 2019-04-15 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_storage.project_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.RemoveField(
            model_name='documentout',
            name='storage_ptr',
        ),
        migrations.RemoveField(
            model_name='documenttest',
            name='storage_ptr',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='polymorphic_ctype',
        ),
        migrations.CreateModel(
            name='ArtProject',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='storage.Project')),
                ('artist', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('storage.project',),
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='storage.Project')),
                ('supervisor', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('storage.project',),
        ),
        migrations.DeleteModel(
            name='DocumentIn',
        ),
        migrations.DeleteModel(
            name='DocumentOut',
        ),
        migrations.DeleteModel(
            name='DocumentTest',
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
    ]
