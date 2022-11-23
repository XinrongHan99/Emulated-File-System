# Generated by Django 3.2.16 on 2022-11-22 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paths',
            fields=[
                ('inode', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('pathType', models.CharField(choices=[('FILE', 'FILE'), ('DIRECTORY', 'DIRECTORY')], default='FILE', max_length=9)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'Paths',
            },
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childInode', to='home.paths')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentInode', to='home.paths')),
            ],
            options={
                'db_table': 'Relations',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('inode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paths')),
            ],
            options={
                'db_table': 'Part',
            },
        ),
    ]