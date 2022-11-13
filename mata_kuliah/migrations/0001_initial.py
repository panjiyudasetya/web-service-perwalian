# Generated by Django 3.2.16 on 2022-11-13 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dosen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=152)),
                ('sks', models.PositiveIntegerField()),
                ('dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosen.dosen')),
            ],
        ),
    ]