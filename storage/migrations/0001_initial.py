# Generated by Django 2.2 on 2019-04-17 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('warehouse', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentPlanIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.WarehouseCell', verbose_name='Адрес приемки')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.WarehouseCell')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_storage.storage_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='DocumentPlanInProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.IntegerField(verbose_name='Плановое количество базовых едениц')),
                ('fact', models.IntegerField(verbose_name='Фактическое количество базовых едениц')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.DocumentPlanIn')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Товар')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.StorageUnit', verbose_name='Единица хранения')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentIn',
            fields=[
                ('storage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='storage.Storage')),
                ('quantity', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('doc_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.DocumentPlanIn')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('storage.storage',),
        ),
    ]