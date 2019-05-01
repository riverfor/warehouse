# Generated by Django 2.2 on 2019-05-01 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190501_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('blocked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='ds',
        ),
        migrations.DeleteModel(
            name='TNod',
        ),
        migrations.AddField(
            model_name='user',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Warehouse'),
        ),
    ]
